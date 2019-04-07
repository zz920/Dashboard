from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    link = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
