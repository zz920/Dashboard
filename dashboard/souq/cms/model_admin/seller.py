from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class HotSellerAdmin(admin.ModelAdmin):

    fields = ('name', 'short_link', 'total_sales', 'check_hot_items', 'related_category', )
    list_display = ('name', 'hot_items')
    search_fields = ['name',]

    list_per_page = 50
    view_on_site = True

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser:
            return self.list_display_links
        else:
            return (None,)

    def hot_items(self, instance):
        return mark_safe('<a href="/souq/hotitem/?seller={}">Check hot item</a>'.format(instance.id))
    hot_items.short_description = _("Hot Items in last 5 days")

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
