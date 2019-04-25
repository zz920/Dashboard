from urllib import parse
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.contrib import admin
from django.db.models import Max, Sum, Q, Value
from django.db.models.functions import Coalesce
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList


class HotItemChangeList(ChangeList):
    LIMIT = 30

    def get_queryset(self, request, **kwargs):
        qs = super().get_queryset(request, **kwargs)
        day_limit = datetime.now() - timedelta(days=5) 
        sum_sales = Sum('detail__sales', filter=Q(detail__created__gte=day_limit))

        filter_query = {}
        if request.GET.get('category'):
            filter_query = {'category__id': request.GET.get('category')}
        elif request.GET.get('seller'):
            filter_query = {'seller__id': request.GET.get('seller')}
        else:
            parser = parse.urlparse(request.META.get('HTTP_REFERER'))
            param = parse.parse_qs(parser.query).get('_changelist_filters')
            if param and param[0]:
                field, id = tuple(param[0].split('='))
                filter_query = {field + '__id': id}
    
        qs = qs.filter(**filter_query).annotate(sum_value=Coalesce(sum_sales, Value(0))).order_by('-sum_value')
        return qs[:self.LIMIT]


class HotItemProxyAdmin(admin.ModelAdmin):

    list_display = ('product_img', 'name', 'link', 'ean_code', 'plantform', 'brand')
    exclude = ('img_link', 'seller', 'detail')
    list_per_page = 10
    view_on_site = True

    change_form_template = 'admin/item_view.html'

    def get_changelist(self, request, **kwargs):
        return HotItemChangeList

    def product_img(self, instance):
        if instance.img_link:
            return mark_safe('<img src="{}" height="60" width="40">'.format(instance.img_link))
        return mark_safe('<img src="" height="60" width="40">')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(**self.model.objects.get(id=object_id).get_detail_list())
        return super().change_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
