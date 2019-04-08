from django.core.management.base import BaseCommand

from souq.models import Category, Seller, Item, Detail
from souq.mongo_models import MCategory, MSeller, MItem
from common.utils.time import timeit


class Command(BaseCommand):
    help = 'Migrate data from spider db.'
    cache = {}

    def handle(self, *args, **options):
        self.migrate_category()
        self.migrate_seller()
        self.migrate_item()

    @timeit
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
        model.objects.bulk_create(create_list)
        print("{} Objects / {}".format(repr(model), len(create_list)))

        # update cache
        local_ext = model.objects.filter(**{uk + '__in': unique_key}).all()
        tmp_cache = {getattr(d, uk): d for d in local_ext}
        for obj in mongo_objs:
            self.cache[obj._id] = tmp_cache[getattr(obj, uk)]


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

    def migrate_item(self):
        from bson.objectid import ObjectId
        def f(x):
            if x is None:
                return ''
            if isinstance(x, bytes):
                return x.decode('utf-8', 'ignore')
            if isinstance(x, ObjectId):
                return self.cache[x]
            return x

        for category in MCategory.objects.all():
            self.common_migration(
                query=MItem.objects.filter(category=category._id).all,
                uk='link',
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
                    'description': 'description',
                    'seller': 'seller',
                },
                f=f
            )
    """
    def test(self):

        for category in MCategory.objects.all():
            print(MItem.objects.filter(category=category._id).count())

            create_list = []
            items = MItem.objects.filter(category=category._id).all():

            for item in items:
                create_list.append()
                tm, _ = Item.objects.update_or_create(
                        link=item.link,
                        defaults={**dict(
                            name=item.name or '',
                            img_link=item.img_link or '',
                            plantform=item.plantform or '',
                            category=cache[item.category],
                            brand=item.brand or '',
                            ean_code=item.ean_code or '',
                            trace_id=item.trace_id or '',
                            description=item.description or '',
                            seller=cache[item.seller],
                        )}
                    )
                except:
                    tm, _ = Item.objects.update_or_create(
                        link=item.link,
                        defaults={**dict(
                            name=item.name or '',
                            img_link=item.img_link or '',
                            plantform=item.plantform or '',
                            category=cache[item.category],
                            brand=item.brand or '',
                            ean_code=item.ean_code or '',
                            trace_id=item.trace_id or '',
                            description='',
                            seller=cache[item.seller],
                        )}
                    )

                for detail in item.detail:
                    dtl, _ = Detail.objects.update_or_create(
                        item=tm, created=detail.created,
                        defaults={**dict(
                            price=detail.price,
                            quantity=detail.quantity
                        )}
                    )
        """
