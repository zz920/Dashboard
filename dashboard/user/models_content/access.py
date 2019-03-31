from django.db import models
from common.models_content.base_model import BaseModel


class Access(BaseModel):
    name = models.CharField(max_length=30)
    description = models.TextField(help_text='description of access')

    class Meta:
        verbose_name_plural = 'Role Access'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
