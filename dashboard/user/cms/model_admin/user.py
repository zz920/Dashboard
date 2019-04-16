from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from common.cms.model_admin.base import BaseModelAdmin


class UserModelAdmin(UserAdmin, BaseModelAdmin):

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
