from django.contrib import admin

from souq.models import Category, Seller, Item

from souq.admin.category import CategoryAdmin
from souq.admin.seller import SellerAdmin
from souq.admin.item import ItemAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Item, ItemAdmin)
