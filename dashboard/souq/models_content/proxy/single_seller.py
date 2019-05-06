from datetime import datetime, timedelta
from collections import Counter
from django.db.models import Max, Sum, F, FloatField
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from souq.models_content.seller import Seller
from souq.models_content.item import Item, Detail


class SingleSeller(Seller):

    def total_sales(self):
        day_limit = datetime.now() - timedelta(days=7)
        sum_value = Sum(F('sales')*F('price'), output_field=FloatField())
        total = Detail.objects.filter(item__seller=self, created__gte=day_limit).aggregate(total=sum_value)['total']
        if not total:
            total = "0"
        return "{} AED in last 7 days".format(total)
    total_sales.short_description = _("Total Sales")

    def related_category(self):
        category = Counter(self.item_set.values_list('category__id', 'category__name'))
        context = []

        for cat, num in category.most_common(5):
            context.append('<a href="/souq/hotitem/?category={}">{} ({} items)</a>'.format(cat[0], cat[1], num))
        if context:
            context.append('In Total {} Category.'.format(len(category)))
        return mark_safe("<br>".join(context)) or "Empty"
    related_category.short_description = _("Related Category")

    def check_hot_items(self):
        return mark_safe('<a href="/souq/hotitem/?seller={}">Check hot item</a>'.format(self.id))
    check_hot_items.short_description = _("Check hot items")

    def short_link(self):
        return mark_safe('<a href="{}">Seller Link</a>'.format(self.link))
    short_link.short_description = _("Short Link")

    class Meta:
        proxy = True
