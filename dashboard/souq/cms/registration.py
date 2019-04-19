from django.contrib import admin

from souq.cms.model_admin import ItemProxyAdmin, HotCategoryAdmin, HotSellerAdmin, HotItemProxyAdmin
from souq.models import Item, Category, Seller, HotItem


admin.site.register(Item, ItemProxyAdmin)
admin.site.register(HotItem, HotItemProxyAdmin)
admin.site.register(Category, HotCategoryAdmin)
admin.site.register(Seller, HotSellerAdmin)
