from django.db import models


class Seller(models.Model):

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name
