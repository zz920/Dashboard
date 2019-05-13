from django.db import models

from common.models_content.base_model import BaseModel
from user.models_content.user import User
from souq.models_content.item import Item

from django.utils.translation import gettext_lazy as _


class UserCollection(BaseModel):

    item_collections = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_collection'
        verbose_name = _('user collection')
        verbose_name_plural = _('user collection')


class UserService(BaseModel):

    class Meta:
        abstract = True
        db_table = 'user_service'
        verbose_name = _('user service')
        verbose_name_plural = _('user service')
