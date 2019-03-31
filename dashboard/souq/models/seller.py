from djongo import models
from .base import ReadOnlyMixin


class Seller(models.Model, ReadOnlyMixin):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250, blank=False, unique=True)

    class Meta:
        db_table = 'seller'
