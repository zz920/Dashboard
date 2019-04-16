from django.contrib import admin

from souq.cms.model_admin import ItemProxyAdmin, HotCategoryAdmin, HotSellerAdmin
from souq.models import Item, Category, Seller


admin.site.register(Item, ItemProxyAdmin)
admin.site.register(Category, HotCategoryAdmin)
admin.site.register(Seller, HotSellerAdmin)
