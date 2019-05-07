from souq.models_content.category import Category
from django.utils.translation import gettext_lazy as _


class SingleCategory(Category):
    
    class Meta:
        proxy = True
        verbose_name = _('Category')
