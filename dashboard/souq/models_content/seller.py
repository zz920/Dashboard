from django.db import models
from django.utils.translation import gettext_lazy as _


class Seller(models.Model):

    name = models.CharField(_('seller name'), max_length=50)
    link = models.CharField(_('seller link'), max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'seller'
        verbose_name_plural = 'sellers'
