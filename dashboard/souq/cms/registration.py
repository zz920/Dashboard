from django.contrib import admin

from souq.cms.model_admin import ItemProxyAdmin
from souq.models import Item


admin.site.register(Item, ItemProxyAdmin)
