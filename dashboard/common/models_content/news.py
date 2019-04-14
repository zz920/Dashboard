from django.db import models
from ckeditor.fields import RichTextField

from .base_model import BaseModel


class News(BaseModel):

    title = models.CharField(max_length=300)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "news"
