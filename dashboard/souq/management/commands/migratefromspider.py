from django.core.management.base import BaseCommand

from souq.models import Category, Seller, Item, Detail
from souq.mongo_models import MCategory, MSeller, MItem



class Command(BaseCommand):
    help = 'Migrate data from spider db.'

    def handle(self, *args, **options):
        cache = {}
        for category in MCategory.objects.all():
            ctgry, _ = Category.objects.update_or_create(
                link=category.link,
                defaults={**dict(
                    name=category.name,
                    classification=category.classification,
                )}
            )
            cache[category._id] = ctgry
        print(len(cache))
        for seller in MSeller.objects.all():
            sllr, _ = Seller.objects.update_or_create(
                link=seller.link,
                defaults={**dict(
                    name=seller.name,
                )}
            )
            cache[seller._id] = sllr
        print(len(cache))
        for category in MCategory.objects.all():
            print(category)
            print(MItem.objects.filter(category=category._id).count())
            for item in MItem.objects.filter(category=category._id).all():
                try:
                    tm, _ = Item.objects.update_or_create(
                        link=item.link,
                        defaults={**dict(
                            name=item.name or '',
                            img_link=item.img_link or '',
                            plantform=item.plantform or '',
                            category=cache[item.category],
                            brand=item.brand or '',
                            ean_code=item.ean_code or '',
                            trace_id=item.trace_id or '',
                            description=item.description or '',
                            seller=cache[item.seller],
                        )}
                    )
                except:
                    tm, _ = Item.objects.update_or_create(
                        link=item.link,
                        defaults={**dict(
                            name=item.name or '',
                            img_link=item.img_link or '',
                            plantform=item.plantform or '',
                            category=cache[item.category],
                            brand=item.brand or '',
                            ean_code=item.ean_code or '',
                            trace_id=item.trace_id or '',
                            description='',
                            seller=cache[item.seller],
                        )}
                    )

                for detail in item.detail:
                    dtl, _ = Detail.objects.update_or_create(
                        item=tm, created=detail.created,
                        defaults={**dict(
                            price=detail.price,
                            quantity=detail.quantity
                        )}
                    )

