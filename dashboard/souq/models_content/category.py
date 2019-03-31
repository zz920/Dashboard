from djongo import models
from .base import ReadOnlyMixin


class Category(models.Model, ReadOnlyMixin):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
