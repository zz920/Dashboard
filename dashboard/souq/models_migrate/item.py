from djongo import models
from django import forms

from souq.models_migrate.seller import MSeller
from souq.models_migrate.category import MCategory


class MDetail(models.Model):

    created = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()

    buybox = models.BooleanField()
    sales = models.IntegerField()


class MItem(models.Model):

    _id = models.ObjectIdField()

    name = models.CharField(max_length=1000)
    img_link = models.CharField(max_length=1000, null=True, blank=True)
    link = models.CharField(max_length=1000)

    plantform = models.CharField(max_length=20)
    category = models.GenericObjectIdField()
    brand = models.CharField(max_length=50, null=True, blank=True)
    ean_code = models.CharField(max_length=50)
    trace_id = models.CharField(max_length=30)
    unit_id = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    seller = models.GenericObjectIdField()
    detail = models.ArrayModelField(
            model_container=MDetail,
            #model_form_class=DetailForm
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item'
    """
    Consider the use case here:
    1. search by the ean_code.
    2. search by the similar name.
    3. search by the category.
    4. search by the brand.
    5. search by the seller.
    """

    def get_detail_list(self):
        ds = [(d.created, d.quantity, d.price) for d in self.detail]
        ds.sort(key=lambda x: x[0])
        date = [d[0].strftime('%Y-%m-%d') for d in ds]
        quantity = [d[1] for d in ds]
        price = [d[2] for d in ds]
        sell = [0] + [max(ds[i-1][1] - ds[i][1], 0) for i in range(1, len(ds))]
        return dict(date=date, price=price, sell=sell, quantity=quantity)
