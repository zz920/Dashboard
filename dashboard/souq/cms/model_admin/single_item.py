from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList

from common.cms.mixin.view_only import ViewOnlyMixin


class SingleItemChangeList(ChangeList):

    def get_queryset(self, request, **kwargs):
        qs = super().get_queryset(request, **kwargs)
        if request.GET.dict():
            # only list the item showing the page
            return qs.filter(link__endswith='i/')
        return qs.none()


class SingleItemProxyAdmin(ViewOnlyMixin, admin.ModelAdmin):

    list_display = ('product_img_small', 'name', 'link', 'ean_code', 'plantform', 'brand')
    fields = ('product_img', 'name', 'short_link', 'ean_code', 'plantform', 'brand')
    exclude = ('img_link', 'seller', 'detail')
    search_fields = ['link__exact', 'ean_code__exact']
    readonly_fields = ('product_img',)
    view_on_site = True

    change_form_template = 'admin/single_item_view.html'

    def get_changelist(self, request, **kwargs):
        return SingleItemChangeList

    def product_img_small(self, instance):
        if instance.img_link:
            return mark_safe('<img src="{}" height="60" width="40">'.format(instance.img_link))
        return mark_safe('<img src="" height="60" width="40">')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(**self.model.get_group_detail_list(id=object_id))
        return super().change_view(request, object_id, form_url, extra_context)

