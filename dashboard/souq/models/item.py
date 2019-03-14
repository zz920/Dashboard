from django.db import models

from .category import Category
from .seller import Seller


class SouqItem(models.Model):

    trace_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=250, db_index=True)
    description = models.CharField(max_length=500)

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
