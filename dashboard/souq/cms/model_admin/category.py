from django.contrib import admin

from django.utils.safestring import mark_safe


class HotCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'classification', 'hot_items')
    search_fields = ['name', 'classification', 'link']

    list_per_page = 50
    view_on_site = True

    """
    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser:
            return self.list_display_links
        else:
            return (None,)
    """

    def hot_items(self, instance):
        return mark_safe('<a href="/souq/hotitem/?category={}">Check hot item</a>'.format(instance.id))
    hot_items.short_description = "hot items"

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
