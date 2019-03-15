import pymongo

from django.core.management.base import BaseCommand, CommandError
from souq.models import Category, Detail, SouqItem, Seller


class Command(BaseCommand):

    help = 'Migrate the data from spider db.'

    def add_arguments(self, parser):
        # 'mongodb://localhost:43815'  'souq'
        parser.add_argument('mongo_db_uri', type=str, default='mongodb://localhost:43815')
        parser.add_argument('mongo_db_name', type=str, default='souq')

    def bulk_create(self, obj, data, size=998):
        if len(data) > size:
            print("Update batch of {}, size {}".format(repr(obj), size))
            obj.objects.bulk_create(data)
            return []
        return data

    def handle(self, *args, **options):
        source = pymongo.MongoClient(options['mongo_db_uri'])[options['mongo_db_name']]

        # insert or update category
        category_collection = source['Category']

        category_cache = {cg.name: '' for cg in Category.objects.all()}
        category_data = []

        for cg in category_collection.find():
            name = cg['name'].lower()
            if name not in category_cache:
                category_data.append(Category(name=name, link=self.clean_url(cg['link']), classification=cg['parent']))
                category_cache[name] = ''
                category_data = self.bulk_create(Category, category_data)
        self.bulk_create(Category, category_data, 0)
        print('Updated all category.')

        item_collection = source['Souqitem']

        seller_cache = {sr.link: '' for sr in Seller.objects.all()}
        seller_data = []

        for seller in item_collection.aggregate([{'$group': {'_id': {"link": "$seller_link"}, "name": {'$first': "$seller"}}}], allowDiskUse=True):
            link = self.clean_url(seller['_id']['link'])
            if link not in seller_cache:
                seller_data.append(Seller(link=link, name=seller['name']))
                seller_cache[link] = ''
                seller_data = self.bulk_create(Seller, seller_data)
        self.bulk_create(Seller, seller_data, 0)

        seller_cache = {sr.link: sr for sr in Seller.objects.all()}
        print('Updated all seller.')

        item_cache = {it.trace_id: '' for it in SouqItem.objects.all()}
        item_data = []

        for item in item_collection.aggregate([{'$group':{'_id': {"trace_id": "$trace_id"}, "name": {'$first': "$name"},
            "link": {"$first": "$link"}, "description": {"$first": "$description"},
                "seller": {"$first": "$seller_link"}, "category": {"$first": "$category"}}}], allowDiskUse=True):
            category = item['category'] or 'default'
            link = self.clean_url(item['link'])
            s_link = self.clean_url(item['seller'])
            if item['_id']['trace_id'] not in item_cache:
                item_data.append(SouqItem(trace_id=item['_id']['trace_id'], name=item['name'], link=link,
                         description=self.clean_str(item['description']), seller=seller_cache.get(s_link),
                         category=category.lower()))
                item_cache[item['_id']['trace_id']] = ''
                item_data = self.bulk_create(SouqItem, item_data)

        item_cache = {}
        seller_cache = {}
        self.bulk_create(SouqItem, item_data, 0)
        print('Updated all item.')


        detail_cache = {d.uid: '' for d in Detail.objects.all()}
        detail_data = []

        for detail in item_collection.aggregate([{'$group':{
                '_id': {"trace_id": "$trace_id"},
                'uid': {'$addToSet': "$_id"},
                'time': {'$addToSet': "$create_at"},
                'price': {'$addToSet': "$price"},
                'quantity': {'$addToSet': "$quantity"},
            }}], allowDiskUse=True):
            item = SouqItem.objects.get(detail['_id']['trace_id'])
            for u, t, p, q in zip(detail['uid'], detail['time'], detail['price'], detail['quantity']):
                if u not in detail_cache:
                    detail_data.append(Detail(uid=u, time=t, price=p, quantity=q))
                    detail_cache[u] = ''
            detail_data = self.bulk_create(Detail, detail_data)
        self.bulk_create(Detail, detail_data, 0)
        print("Done.")

    def clean_url(self, url):
        while url.startswith('/'):
            url = url[1:]
        if not url.startswith('https://'):
            url = 'https://uae.souq.com/' + url
        return url

    def clean_str(self, string):
        return string.encode('utf-8', 'ignore').decode('utf-8')
