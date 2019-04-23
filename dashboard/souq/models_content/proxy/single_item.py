from souq.models_content.item import Item


class SingleItem(Item):

    class Meta:
        proxy = True
