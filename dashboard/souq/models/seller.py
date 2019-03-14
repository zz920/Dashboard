from django.db import models


class Seller(models.Model):

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250, db_index=True)
