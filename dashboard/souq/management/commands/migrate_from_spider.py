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

        item_collection = source['Souqitem']

        seller_cache = {sr.link: '' for sr in Seller.objects.all()}
        seller_data = []

        for seller in item_collection.aggregate([{'_id': {"link": "$seller_link"}, "name": {'$first': "$seller"}}]):
            if seller['link'] not in seller_cache:
                seller_data.append(Seller(link=seller['link'], name=seller['name']))
            if len(seller_data) > 998:
                Seller.objects.bulk_create(seller_data)
                seller_data = []

        if len(seller_data):
                Seller.objects.bulk_create(seller_data)
                seller_data = []
        seller_cache = {sr.link: sr for sr in Seller.objects.all()}

        print('Updated {} seller'.format(len(seller_cache)))

        item_cache = {it.trace_id: '' for it in SouqItem.objects.all()}
        item_data = []

        for item in item_collection.aggregate([{'_id': {"trace_id": "$trace_id"}, "name": {'$first': "$name"},
            "link": {"$first": "$link"}, "description": {"$first": "$description"},
                "seller": {"$first": "$seller_link"}, "category": {"$first": "$category"}}]):
            category = item['category'] or 'default'
            if item['trace_id'] not in item_cache:
                item_data.append(SouqItem(trace_id=item['trace_id'], name=item['name'], link=self.clean_url(item['link']),
                         description=item['description'], seller=seller_cache.get(item["seller_link"]),
                         category=category.lower()))
            if len(item_data) > 998:
                SouqItem.objects.bulk_create(item_data)
                item_data = []
        if len(item_data):
            SouqItem.objects.bulk_create(item_data)
            item_data = []
        print("Done.")

    def clean_url(self, url):
        while url.startswith('/'):
            url = url[1:]
        if not url.startswith('https://'):
            url = 'https://uae.souq.com/' + url
        return url
