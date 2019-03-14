from django.db import models

from .item import SouqItem

class Detail(models.Model):

    uid = models.CharField(max_length=50, unique=True)
    time = models.DateField(db_index=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    item = models.ForeignKey(SouqItem, on_delete=models.CASCADE)
