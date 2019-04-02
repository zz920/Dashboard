from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models_content.base_model import BaseModel


class User(AbstractUser, BaseModel):

    phone_number = models.CharField(max_length=45)

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'users'

    @classmethod
    def get_user_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_user_by_username(cls, username):
        try:
            return cls.objects.get(username=username)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_user_by_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None
