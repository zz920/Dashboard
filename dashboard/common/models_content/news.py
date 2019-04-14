import mistune
from django.db import models
from .base_model import BaseModel


class News(BaseModel):

    title = models.CharField(max_length=300)
    raw_content = models.TextField() 
    html_content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.html_content = mistune.Markdown()(self.raw_content)
        return super(News, self).save(**kwargs)

    @property
    def content(self):
        if self.html_content:
            return self.html_content
        return self.raw_content

    class Meta:
        verbose_name_plural = "news"
