from souq.mongo_models import MCategory, MItem, MSeller
from souq.models import *


class CustomDBRouter(object):
    SOUQ_MONGO_MODEL = (MCategory, MItem, MSeller)
    SOUQ_PSQL_MODEL = (Category, Item, Seller, Detail)
    SOUQ_PSQL_PROXY_MODEL = (HotItem, SingleItem, SingleCategory, SingleSeller)

    def db_for_read(self, model, **hints):
        if model in self.SOUQ_MONGO_MODEL:
            return 'mongo_souq_ksa'
        if model in self.SOUQ_PSQL_MODEL or model in self.SOUQ_PSQL_PROXY_MODEL:
            return 'psql_souq_ksa'
        return None

    def db_for_write(self, model, **hints):
        if model in self.SOUQ_MONGO_MODEL:
            return 'mongo_souq_ksa'
        if model in self.SOUQ_PSQL_MODEL or model in self.SOUQ_PSQL_PROXY_MODEL:
            return 'psql_souq_ksa'
        return None
