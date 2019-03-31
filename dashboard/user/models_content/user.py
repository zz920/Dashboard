from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models_content.base_model import BaseModel
from .role import Role


class User(AbstractUser, BaseModel):
    # move to enum
    ADMIN = 1
    CLIENT_USER = 2
    FETCHR_USER = 3

    USER_TYPE_CHOICES = ((ADMIN, 'Admin'), (CLIENT_USER, 'Client User'), (FETCHR_USER, 'Fetchr User'),)
    phone_number = models.CharField(max_length=45)
    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=ADMIN)
    roles = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)

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

    @property
    def role(self):
        return self.roles.name
