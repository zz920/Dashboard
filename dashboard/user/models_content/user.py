from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models_content.base_model import BaseModel


class UserAuthManager(UserManager):
    use_in_migrations = True

    def create_superuser(self, username, email, password, **extra_fields):
        user = super(UserAuthManager, self).create_superuser(username, email, password, **extra_fields)
        user.save()
        return user

    def create_admin_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_customer_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, BaseModel):

    phone_number = models.CharField(max_length=45)

    objects = UserAuthManager()

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

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
