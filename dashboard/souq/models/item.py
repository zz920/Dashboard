from djongo import models
from django import forms

from dashboard.souq.models import Seller, Category 


class Detail(models.Model):
    
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


class Item(models.Model):

    _id = models.ObjectIdField()
    created = models.DateField()

    name = models.CharField()
    img_link = models.CharField()
    link = models.CharField()

    plantform = models.CharField()
    category = models.ForeignKey(Category)
    brand = models.CharField()
    ean_code = models.CharField()
    trace_id = models.CharField()
    description = models.CharField()

    seller = models.ForeignKey(Seller)
    detail = models.ArrayModelField(
            model_container=Detail,
            model_form_class=DetailForm
    )

    """
    Consider the use case here:
    1. search by the ean_code.
    2. search by the similar name.
    3. search by the category.
    4. search by the brand.
    5. search by the seller.
    """
