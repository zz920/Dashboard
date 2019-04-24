from django.utils.safestring import mark_safe
from souq.models_content.item import Item


class SingleItem(Item):

    @property
    def product_img(self):
        if self.img_link:
            return mark_safe('<img src="{}">'.format(self.img_link))
        return mark_safe('<img src="" height="40" width="40">')

    @property
    def short_link(self):
        return mark_safe('<a href="{}">Production Link</a>'.format(self.link))

    @classmethod
    def get_group_detail_list(cls, id):
        """
        We could give this detail a longer period query to show the difference between the different seller.
        """
        obj = cls.objects.filter(id=id).first()
        if not obj:
            return {}
        bunch = cls.objects.filter(trace_id=obj.trace_id).all()
        if not bunch:
            return {}

        bunch_data = []
        for item in bunch:
            seller_data = {'name': item.seller.name, 'link': item.seller.link}
            item_data = item.get_detail_list()
            bunch_data.append({'seller': seller_data, 'item': item_data})
        return {'bunch': bunch_data}

    class Meta:
        proxy = True
