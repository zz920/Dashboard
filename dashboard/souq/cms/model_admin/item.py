from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList


class ItemChangeList(ChangeList):
    def get_queryset(self, request):
        queryset = super(ItemChangeList, self).get_queryset(request)
        return queryset[:50]


class ItemProxyAdmin(admin.ModelAdmin):

    list_display = ('product_img', 'name', 'link', 'ean_code', 'plantform', 'brand')
    exclude = ('_id', 'img_link', 'category', 'seller', 'detail')
    search_fields = ['link', 'ean_code']
    list_per_page = 30

    def product_img(self, instance):
        if instance.img_link:
            return mark_safe('<img src="{}" height="60" width="40">'.format(instance.img_link[21:]))
        return mark_safe('<img src="{}" height="60" width="40">')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
