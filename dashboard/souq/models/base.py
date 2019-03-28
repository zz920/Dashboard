class BaseModelPlugin():
    """
    Basic model method
    """
    @classmethod
    def create_or_update(cls, **kwargs):
        upsert_kwargs = {
            'set__' + k : v
            for k, v in kwargs.items()
        }
        return cls.objects(**kwargs).modify(
            upsert=True, new=True,
            **upsert_kwargs
        )

    @classmethod
    def get(cls, **kwargs):
        return cls.objects(**kwargs).first()
