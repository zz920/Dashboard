from djongo import models


class Seller(models.Model):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250, blank=False, unique=True)
