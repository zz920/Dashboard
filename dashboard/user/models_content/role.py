from django.db import models

from common.models_content.base_model import BaseModel
from .access import Access


class Role(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(help_text="What does this role do")
    access = models.ManyToManyField(Access, related_name="access")

    class Meta:
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
