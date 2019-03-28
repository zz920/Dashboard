from djongo import models


class Category(models.Model):

    _id = models.ObjectIdField()
    name = models.CharField()
    classification = models.CharField()
    link = models.CharField()
