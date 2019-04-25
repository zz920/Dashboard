from souq.models_content.seller import Seller


class SingleSeller(Seller):
    
    class Meta:
        proxy = True
