from django.shortcuts import redirect
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import gettext_lazy as _

from common.cms.mixin.view_only import ViewOnlyMixin


class ItemChangeList(ChangeList):
    pass


class ItemProxyAdmin(admin.ModelAdmin, ViewOnlyMixin):

    list_display = ('product_img', 'name', 'ean_code', 'plantform', 'brand')
    exclude = ('img_link', 'category', 'seller', 'detail')
    search_fields = ['link__exact', 'ean_code__exact', 'brand', 'trace_id']
    list_per_page = 10
    view_on_site = True

    change_form_template = 'admin/item_view.html'

    def get_changelist(self, request, **kwargs):
        return ItemChangeList

    def product_img(self, instance):
        if instance.img_link:
            return mark_safe('<img src="{}" height="60" width="40">'.format(instance.img_link))
        return mark_safe('<img src="" height="60" width="40">')
    product_img.short_description = _('Product Image')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(**self.model.objects.get(id=object_id).get_detail_list())
        return super().change_view(request, object_id, form_url, extra_context)
