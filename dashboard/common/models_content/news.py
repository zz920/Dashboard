from django.db import models
from .base_model import BaseModel


class News(BaseModel):

    title = models.CharField(max_length=300)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "news"
