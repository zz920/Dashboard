from django.contrib.auth.admin import UserAdmin
from common.cms.model_admin.base import BaseModelAdmin


class UserModelAdmin(UserAdmin, BaseModelAdmin):
    pass
