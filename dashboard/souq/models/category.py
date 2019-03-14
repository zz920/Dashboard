from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    classification = models.CharField(max_length=50)
    link = models.CharField(max_length=250, db_index=True)
