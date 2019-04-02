from user.models import Customer
from jet.admin import CompactInline


class CustomerInline(CompactInline):
    model = Customer
    extra = 1
    show_change_link = True
