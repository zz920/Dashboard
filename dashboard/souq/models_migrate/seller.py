from djongo import models


class MSeller(models.Model):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'seller'
