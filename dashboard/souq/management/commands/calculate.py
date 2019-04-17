from django.core.management.base import BaseCommand

from souq.models import Category, Seller, Item, Detail
from common.utils.time import timeit


class Command(BaseCommand):

    @timeit
    def handle(self, *args, **options):
        """
        Calculate the sales data
        """
        item_list = []
        for item in Item.objects.all():
            item_list.append(item)
            if len(item_list) >= 1000:
                self.update_1000_items(item_list)
        self.update_1000_items(item_list)


    @timeit
    def update_1000_items(self, items):
        detail_update = []
        for item in items:
            ds = [(d.created, d.quantity, d) for d in item.detail_set.all()]
            ds.sort(key=lambda x: x[0])
            sales = [0] + [max(ds[i-1][1] - ds[i][1], 0) for i in range(1, len(ds))]
            for d, s in zip(ds, sales):
                d[2].sales = s
                detail_update.append(d[2])
        Detail.objects.bulk_update(detail_update, ['sales'])
