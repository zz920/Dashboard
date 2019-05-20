from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Max, Sum, Q, F, Value, Count, Avg
from django.db.models.functions import Coalesce
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import gettext_lazy as _

from common.cms.mixin.view_only import ViewOnlyMixin


class ItemChangeList(ChangeList):
    def get_queryset(self, request, **kwargs):
        yesterday = datetime.now() - timedelta(1)
        qs = super().get_queryset(request, **kwargs)
        qs = qs.annotate(
                seller_count=Count('trace_id'), 
                total_sales=Coalesce(Sum('detail__sales'), Value(0)), 
                price=Max('detail__price', filter=Q(detail__created=yesterday))
        )
        return qs.order_by('name')


class ItemProxyAdmin(ViewOnlyMixin, admin.ModelAdmin):

    list_display = ('product_img', 'name', 'price', 'seller_count', 'total_sales', 'ean_code', 'plantform', 'brand')
    exclude = ('img_link', 'category', 'seller', 'detail')
    search_fields = ['link__exact', 'ean_code__exact', 'brand', 'trace_id']
    list_per_page = 10
    view_on_site = True

    change_form_template = 'admin/item_view.html'

    def get_changelist(self, request, **kwargs):
        return ItemChangeList

    def get_sortable_by(self, request):
        return {'name', 'seller_count', 'total_sales'}

    def seller_count(self, instance):
        return instance.seller_count
    seller_count.short_description = _('Seller Count')
    seller_count.admin_order_field = 'seller_count'

    def price(self, instance):
        if instance.avg_price:
            return '%.2f' % instance.avg_price 
        return _('Unknown')
    price.short_description = _("Average Price")
    price.admin_order_field = 'avg_price'

    def total_sales(self, instance):
        return instance.total_sales
    total_sales.short_description = _('Total Sales')
    total_sales.admin_order_field = 'total_sales'

    def product_img(self, instance):
        if instance.img_link:
            return mark_safe('<img src="{}" height="60" width="40">'.format(instance.img_link))
        return mark_safe('<img src="" height="60" width="40">')
    product_img.short_description = _('Product Image')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(**self.model.objects.get(id=object_id).get_detail_list())
        return super().change_view(request, object_id, form_url, extra_context)
