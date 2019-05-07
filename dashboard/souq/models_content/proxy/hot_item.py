from souq.models_content.item import Item
from django.utils.translation import gettext_lazy as _


class HotItem(Item):

    class Meta:
        proxy = True
        verbose_name = _('Hot Item')
