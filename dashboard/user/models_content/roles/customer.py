from django.db import models
from user.models_content.user import User


class CustomerManager(models.Manager):
    pass

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = CustomerManager()
