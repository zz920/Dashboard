from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Max, Sum, Q, F, Value, Count, Avg
from django.db.models.functions import Coalesce
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator
from django.utils.functional import cached_property

from common.cms.mixin.view_only import ViewOnlyMixin
from souq.models import Item


class ItemPaginator(Paginator):

    def page(self, number):
        """Return a Page object for the given 1-based page number."""
        number = self.validate_number(number)
        return self._get_page(self.object_list, number, self)

    @cached_property
    def count(self):
        """Return the total number of objects, across all pages."""
        return Item.objects.count()

    def _check_object_list_is_ordered(self):
        pass


class ItemChangeList(ChangeList):
    def get_queryset(self, request, **kwargs):
        limit = 10
        offset = 10 * int(request.GET.get('p', '0'))
        qs = Item.objects.raw("""
            SELECT
                *
            FROM souq_item
            JOIN (
                SELECT
                    trace_id,
                    count(*) as seller_count
                FROM souq_item
                GROUP BY trace_id
            ) t1 ON souq_item.trace_id=t1.trace_id offset {} limit {}
        """.format(offset, limit))
        return qs


class ItemProxyAdmin(ViewOnlyMixin, admin.ModelAdmin):

    list_display = ('product_img', 'name', 'price', 'seller_count', 'total_sales', 'ean_code', 'plantform', 'brand')
    exclude = ('img_link', 'category', 'seller', 'detail')
    search_fields = ['link__exact', 'ean_code__exact', 'brand', 'trace_id']
    list_per_page = 10
    view_on_site = True

    paginator = ItemPaginator
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
        try:
            return '%.2f' % instance.detail_set.first().price
        except:
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
