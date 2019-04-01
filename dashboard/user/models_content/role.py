from django.db import models

from common.models_content.base_model import BaseModel
from common.enum.role import SystemValidRole
from .access import Access


class Role(BaseModel):

    role_type = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in SystemValidRole], default=SystemValidRole.VISITOR)
    description = models.TextField(help_text="What does this role do")
    access = models.ManyToManyField(Access, related_name="access")

    class Meta:
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
