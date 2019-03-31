from souq.models import Category, Item, Seller


class CustomDBRouter(object):
    SOUQ_MODEL = (Category, Item, Seller)

    def db_for_read(self, model, **hints):
        if model in self.SOUQ_MODEL:
            return 'souq'
        return None

    def db_for_write(self, model, **hints):
        if model in self.SOUQ_MODEL:
            return 'souq'
        return None
