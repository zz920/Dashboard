from django.db import models
from common.models_content.base_model import BaseModel
from common.enum.access import SystemValidAccess


class Access(BaseModel):
    access_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in SystemValidAccess], default=SystemValidAccess.NO_ACCESS)
    description = models.TextField(help_text='description of access')

    class Meta:
        verbose_name_plural = 'Role Access'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
