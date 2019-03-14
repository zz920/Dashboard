import pymongo

from django.core.management.base import BaseCommand, CommandError
from souq.models import Category, Detail, SouqItem, Seller


class Command(BaseCommand):

    help = 'Migrate the data from spider db.'

    def add_arguments(self, parser):
        # 'mongodb://localhost:43815'  'souq'
        parser.add_argument('mongo_db_uri', type=str, default='mongodb://localhost:43815')
        parser.add_argument('mongo_db_name', type=str, default='souq')

    def cache_get(self, obj, query=True, **options):
        cache_name = 'cache' + repr(obj)
        if not hasattr(self, cache_name):
            setattr(self, cache_name, {})
        cache = getattr(self, cache_name)

        key = repr({**options})
        if key not in cache and query:
            try:
                cache[key] = obj.objects.get(**options)
            except obj.DoesNotExist:
                pass
        return cache.get(key)

    def get_or_create(self, obj, defaults={}, query=True, **options):
        options = self.clean_arabic(options)
        defaults.update(**options)
        _obj = self.cache_get(obj, query=query, **options)
        if not _obj:
            _obj = obj(**defaults)
            _obj.save()
        return self.cache_get(obj, **options)


    def clean_arabic(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = v.encode('utf-8', 'ignore').decode('utf-8')
        return data

    def handle(self, *args, **options):
        source = pymongo.MongoClient(options['mongo_db_uri'])[options['mongo_db_name']]

        # insert or update category
        category_collection = source['Category']
        count = 0
        for cg in category_collection.find():
            count += 1
            if count % 1000 == 0: print('Updated {} category'.format(count))

            name = cg['name'].lower()
            obj = self.get_or_create(Category, name=name, defaults={
                'link': self.clean_url(cg['link']),
                'classification': cg['parent']
            })

        count = 0
        item_collection = source['Souqitem']
        # initial the cache
        self.cache_get(SouqItem, trace_id="test")
        item_cache = getattr(self, 'cache' + repr(SouqItem))
        for it in SouqItem.objects.all():
            item_cache[repr({'trace_id': it.trace_id})] = it

        data = {}
        for it in item_collection.find():
            count += 1
            if count % 10000 == 0:
                print('Updated {} item'.format(count))

            seller = self.get_or_create(
                Seller,
                link=self.clean_url(it['seller_link']),
                defaults={'name': it['seller']}
            )
            category = it['category'] or 'default'

            trace_id = it['trace_id']
            if trace_id not in item_cache:
                data[trace_id] = SouqItem(
                    trace_id=trace_id,
                    name=it['name'],
                    link=self.clean_url(it['link']),
                    description=it['description'],
                    seller=seller,
                    category=category.lower(),
                )
        SouqItem.objects.bulk_create(list(data.values()))

        # to avoid dup detail created
        for it in SouqItem.objects.all():
            details = {d.uid: d for d in it.detail_set.all()}
            data = []
            for _it in item_collection.find({'trace_id': it.trace_id}):
                if _it['_id'] in details:
                    continue
                data.append(
                    Detail(
                        uid=str(_it['_id']),
                        time=_it['create_at'],
                        price=_it['price'],
                        quantity=_it['quantity'],
                        item=it
                    )
                )
            Detail.objects.bulk_create(data)
            print('Updated {} details'.format(len(data)))

    def clean_url(self, url):
        while url.startswith('/'):
            url = url[1:]
        if not url.startswith('https://'):
            url = 'https://uae.souq.com/' + url
        return url
