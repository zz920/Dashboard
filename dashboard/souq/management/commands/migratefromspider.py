import sys

from django_rq import job
from django.core.management.base import BaseCommand

from souq.models import Category, Seller, Item, Detail
from souq.mongo_models import MCategory, MSeller, MItem
from common.utils.time import timeit


@job
def bulk_create_helper(model, obj_list):
    model.object.bulk_create(obj_list)


def sys_progress_print(num):
    sys.stdout.write("\r%.2f%%" % num)
    if int(num) % 20 == 0 and num > 1:
        import ipdb; ipdb.set_trace()
    sys.stdout.flush()


class Command(BaseCommand):
    help = 'Migrate data from spider db.'
    # cache = {}

    @timeit
    def handle(self, *args, **options):
        self.cache = {}
        self.migrate_category()
        self.migrate_seller()
        self.migrate_item()
        self.migrate_detail()

    def common_migration(self, query, uk, model, mapping, f=lambda x: x):
        """
        mapping is local_field: mongo_field
        """
        mongo_objs = query()
        unique_key = [getattr(obj, uk) for obj in mongo_objs]

        local_ext = model.objects.filter(**{uk + '__in': unique_key}).values_list('id', uk)
        uk_set = set([u[1] for u in local_ext])
        create_list = []

        for obj in mongo_objs:
            data = {
                k: f(getattr(obj, v))
                for k, v in mapping.items()
            }
            if getattr(obj, uk) not in uk_set:
                create_list.append(model(**data))
        if create_list:
            # bulk_create_helper.delay(model, create_list)
            model.objects.bulk_create(create_list)
        # if len(create_list):
        #    print("{} Objects / {}".format(repr(model), len(create_list)))

        # update cache
        local_ext = model.objects.filter(**{uk + '__in': unique_key}).all()
        tmp_cache = {getattr(d, uk): d for d in local_ext}
        for obj in mongo_objs:
            try:
                self.cache[obj._id] = tmp_cache[getattr(obj, uk)]
            except:
                print("{} Object missing: {}".format(obj, uk))

    @timeit
    def migrate_category(self):
        def f(x):
            if isinstance(x, bytes):
                return x.decode('utf-8', 'ignore')
            return x

        self.common_migration(
            query=MCategory.objects.all,
            uk='link',
            model=Category,
            mapping={
                'link': 'link',
                'name': 'name',
                'classification': 'classification'
            },
            f=f
        )

    @timeit
    def migrate_seller(self):
        def f(x):
            if isinstance(x, bytes):
                return x.decode('utf-8', 'ignore')
            return x

        self.common_migration(
            query=MSeller.objects.all,
            uk='link',
            model=Seller,
            mapping={
                'link': 'link',
                'name': 'name',
            },
            f=f,
        )

    @timeit
    def migrate_item(self):
        from bson.objectid import ObjectId
        def f(x):
            if x is None:
                return ''
            if isinstance(x, bytes):
                x = x.decode('utf-8', 'ignore')
            if isinstance(x, str):
                x = x.replace('\x00', '')
            if isinstance(x, ObjectId):
                if x not in self.cache:
                    self.migrate_seller()
                return self.cache[x]
            return x
        
        total = MCategory.objects.count()
        for ind, category in enumerate(MCategory.objects.all()):
            self.common_migration(
                query=MItem.objects.filter(category=category._id).all,
                uk='unit_id',
                model=Item,
                mapping={
                    'link': 'link',
                    'name': 'name',
                    'img_link': 'img_link',
                    'plantform': 'plantform',
                    'category': 'category',
                    'brand': 'brand',
                    'ean_code': 'ean_code',
                    'trace_id': 'trace_id',
                    'unit_id': 'unit_id',
                    'description': 'description',
                    'seller': 'seller',
                },
                f=f
            )
            sys_progress_print(float((ind + 1) * 100) / total) 

    @timeit
    def migrate_detail(self):
        detail_cache = set(Detail.objects.values_list('identify', flat=True))
        total = MCategory.objects.count()
        for ind, category in enumerate(MCategory.objects.all()):
            create_list = []
            for item in MItem.objects.filter(category=category._id).all():
                tm = self.cache.get(item._id)
                if not tm:
                    # This case is the spider create new item during the migrations, just ignore it for now.
                    continue

                for detail in item.detail:
                    identify = "{}_{}".format(detail.created, item._id)
                    if identify not in detail_cache:
                        create_list.append(
                            Detail(
                                **dict(
                                    item=tm,
                                    created=detail.created,
                                    price=detail.price,
                                    quantity=detail.quantity,
                                    buybox=detail.buybox,
                                    sales=detail.sales,
                                    identify=identify,
                                )
                            )
                        )
                        # to avoid the same day scrapy twice
                        detail_cache.add(identify)
            # bulk_create_helper.delay(Detail, create_list)
            Detail.objects.bulk_create(create_list)
            sys_progress_print(float((ind + 1) * 100) / total) 
            # print("{} Objects / {}".format(repr(Detail), len(create_list)))
