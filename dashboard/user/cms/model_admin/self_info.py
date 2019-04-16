from django.contrib.auth.admin import UserAdmin
from common.cms.model_admin.base import BaseModelAdmin


class UserSelfInfoModelAdmin(UserAdmin):

    exclude = ['created_at', 'updated_at', 'updated_by']


