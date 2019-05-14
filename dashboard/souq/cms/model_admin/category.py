from django.contrib import admin
from django.utils.safestring import mark_safe

from common.cms.mixin.view_only import ViewOnlyMixin


class HotCategoryAdmin(ViewOnlyMixin, admin.ModelAdmin):

    list_display = ('name', 'classification', 'hot_items')
    search_fields = ['name', 'classification', 'link']

    list_per_page = 50
    view_on_site = True

    def hot_items(self, instance):
        return mark_safe('<a href="/souq/hotitem/?category={}" target="_blank">Check hot item</a>'.format(instance.id))
    hot_items.short_description = "hot items"
