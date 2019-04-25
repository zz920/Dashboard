import architect
from djongo import models
from django import forms
from collections import deque

from souq.models_content.seller import Seller
from souq.models_content.category import Category


class Item(models.Model):

    name = models.CharField(max_length=1000)
    img_link = models.CharField(max_length=1000, null=True, blank=True)
    link = models.CharField(max_length=1000)

    plantform = models.CharField(max_length=20)

    brand = models.CharField(max_length=50, null=True, blank=True)
    ean_code = models.CharField(max_length=50)
    trace_id = models.CharField(max_length=30)
    unit_id = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=1000)


    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['link']),
            models.Index(fields=['ean_code']),
            models.Index(fields=['name']),
            models.Index(fields=['unit_id']),
            models.Index(fields=['trace_id']),
        ]
    """
    Consider the use case here:
    1. search by the ean_code.
    2. search by the similar name.
    3. search by the category.
    4. search by the brand.
    5. search by the seller.
    """

    def get_detail_list(self, date=None):
        if date:
            qs = deque(self.detail_set.filter(created__gte=date[0], created__lte=date[-1]).order_by('created').values_list('created', 'quantity', 'price', 'sales', 'buybox').all())
            ds = []
            for d in date:
                if qs:
                    if d > qs[0][0]:
                        qs.popleft()
                    elif d < qs[0][0]:
                        ds.append((d, None, None, None, None))
                    else:
                        ds.append(qs.popleft())
                else:
                    ds.append((d, None, None, None, None))
        else:
            ds = [d for d in self.detail_set.order_by('created').values_list('created', 'quantity', 'price', 'sales', 'buybox').all()]
        ds.sort(key=lambda x: x[0])
        date = [d[0].strftime('%Y-%m-%d') for d in ds]
        quantity = [d[1] for d in ds]
        price = [d[2] for d in ds]
        sale = [d[3] for d in ds]
        buybox = [d[4] for d in ds]
        total = {'buybox': sum([1 for b in buybox if b]), 'sale': sum([s for s in sale if s])}
        return dict(date=date, price=price, sale=sale, quantity=quantity, buybox=buybox, total=total)


@architect.install('partition', type='range', subtype='integer', constraint='10000', column='item_id')
class Detail(models.Model):

    created = models.DateField()
    price = models.FloatField()
    sales = models.IntegerField(default=0)
    buybox = models.BooleanField()
    quantity = models.IntegerField()
    identify = models.CharField(max_length=50, unique=True)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['identify']),
        ]


