import pymongo

from django.core.management.base import BaseCommand, CommandError
from souq.models import Category, Detail, SouqItem, Seller


class Command(BaseCommand):

    help = 'Migrate the data from spider db.'

    def add_arguments(self, parser):
        # 'mongodb://localhost:43815'  'souq'
        parser.add_argument('mongo_db_uri', type=str, default='mongodb://localhost:43815')
        parser.add_argument('mongo_db_name', type=str, default='souq')

    def handle(self, *args, **options):
        source = pymongo.MongoClient(options['mongo_db_uri'])[options['mongo_db_name']]

        # insert or update category
        category_collection = source['Category']
        count = 0
        for cg in category_collection.find():
            Category.objects.update_or_create(
                link=self.clean_url(cg['link']),
                defaults={'name': cg['name'].lower(), 'classification': cg['parent']}
            )
            count += 1
            if count % 1000 == 0: print('Updated {} category'.format(count))


        count = 0
        item_collection = source['Souqitem']
        for it in item_collection.find():
            seller, _ = Seller.objects.get_or_create(
                link=self.clean_url(it['seller_link']),
                defaults={'name': it['seller']}
            )
            category = Category.objects.get(name=it['category'].lower())
            item, _ = SouqItem.objects.get_or_create(
                trace_id=it['trace_id'],
                defaults={
                    'name': it['name'],
                    'link': self.clean_url(it['link']),
                    'description': it['description'],
                    'seller': seller,
                    'category': category,
                }
            )
            Detail.objects.get_or_create(
                uid=str(it['_id']),
                defaults={
                    'time':it['create_at'],
                    'price': it['price'],
                    'quantity': it['quantity'],
                    'item': item,
                }
            )
            count += 1
            if count % 10000 == 0: print('Updated {} item'.format(count))


    def clean_url(self, url):
        while url.startswith('/'):
            url = url[1:]
        if not url.startswith('https://'):
            url = 'https://uae.souq.com/' + url
        return url
