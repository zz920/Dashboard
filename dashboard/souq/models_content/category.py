from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(_('name'), max_length=50)
    classification = models.CharField(_('classification'), max_length=50)
    link = models.CharField(_('link'), max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
