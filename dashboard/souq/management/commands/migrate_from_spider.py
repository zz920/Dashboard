import pymongo

from django.core.management.base import BaseCommand, CommandError
from souq.models import Category, Detail, SouqItem, Seller


class Command(BaseCommand):

    help = 'Migrate the data from spider db.'

    def add_arguments(self, parser):
        # 'mongodb://localhost:43815'  'souq'
        parser.add_argument('mongo_db_uri', type=str, default='mongodb://localhost:43815')
        parser.add_argument('mongo_db_name', type=str, default='souq')

    def cache_get(self, obj, **options):
        cache_name = 'cache' + repr(obj)
        if not hasattr(self, cache_name):
            setattr(self, cache_name, {})
        cache = getattr(self, cache_name)

        key = repr({**options})
        if key not in cache:
            try:
                cache[key] = obj.objects.get(**options)
            except obj.DoesNotExist:
                pass
            except:
                import ipdb; ipdb.set_trace()
                pass
        return cache.get(key)

    def get_or_create(self, obj, defaults={}, **options):
        options = self.clean_arabic(options)
        defaults.update(**options)
        _obj = self.cache_get(obj, **options)
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
            item = self.get_or_create(
                SouqItem,
                trace_id=it['trace_id'],
                defaults={
                    'name': it['name'],
                    'link': self.clean_url(it['link']),
                    'description': it['description'],
                    'seller': seller,
                    'category': category.lower(),
                }
            )
            try:
                Detail(
                    uid=str(it['_id']),
                    time=it['create_at'],
                    price=it['price'],
                    quantity=it['quantity'],
                    item=item,
                ).save()
            except:
                pass

    def clean_url(self, url):
        while url.startswith('/'):
            url = url[1:]
        if not url.startswith('https://'):
            url = 'https://uae.souq.com/' + url
        return url
