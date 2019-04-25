from django.contrib import admin

from souq.cms.model_admin import ItemProxyAdmin, HotCategoryAdmin, HotSellerAdmin, HotItemProxyAdmin, SingleItemProxyAdmin
from souq.models import Item, SingleCategory, SingleSeller, HotItem, SingleItem


admin.site.register(Item, ItemProxyAdmin)
admin.site.register(HotItem, HotItemProxyAdmin)
admin.site.register(SingleItem, SingleItemProxyAdmin)
admin.site.register(SingleCategory, HotCategoryAdmin)
admin.site.register(SingleSeller, HotSellerAdmin)
