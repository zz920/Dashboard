from djongo import models
from django import forms

from souq.models_content import Seller, Category
from .base import ReadOnlyMixin


class Detail(models.Model, ReadOnlyMixin):

    created = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        abstract = True


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = (
            'created', 'price', 'quantity'
        )


class Item(models.Model, ReadOnlyMixin):

    _id = models.ObjectIdField()
    created = models.DateField()

    name = models.CharField(max_length=1000)
    img_link = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    plantform = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    ean_code = models.CharField(max_length=50)
    trace_id = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    detail = models.ArrayModelField(
            model_container=Detail,
            model_form_class=DetailForm
    )

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
