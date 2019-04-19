from souq.models_content.item import Item


class HotItem(Item):

    class Meta:
        proxy = True
