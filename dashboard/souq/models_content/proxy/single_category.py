from souq.models_content.category import Category


class SingleCategory(Category):
    
    class Meta:
        proxy = True
