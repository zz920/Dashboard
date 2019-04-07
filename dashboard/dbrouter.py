from souq.mongo_models import MCategory, MItem, MSeller


class CustomDBRouter(object):
    SOUQ_MONGO_MODEL = (MCategory, MItem, MSeller)

    def db_for_read(self, model, **hints):
        if model in self.SOUQ_MONGO_MODEL:
            return 'souq'
        return None

    def db_for_write(self, model, **hints):
        if model in self.SOUQ_MONGO_MODEL:
            return 'souq'
        return None
