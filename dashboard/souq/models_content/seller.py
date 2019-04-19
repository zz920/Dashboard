from djongo import models


class Seller(models.Model):

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    def get_hot_items(self, limit=30):
        items = [t for t in self.item_set.all()]


