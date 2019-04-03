from django.contrib.auth.admin import UserAdmin
from common.cms.model_admin.base import BaseModelAdmin


class UserModelAdmin(UserAdmin, BaseModelAdmin):
    # TODO: overwrite the UserAdmin, with permission(redirecting) and add more fields(phone number)
    pass
