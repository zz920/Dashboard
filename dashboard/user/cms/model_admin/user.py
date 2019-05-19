from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from common.cms.model_admin.base import BaseModelAdmin
from common.cms.mixin.super_only import SuperOnlyMixin


class UserModelAdmin(SuperOnlyMixin, UserAdmin, BaseModelAdmin):
    pass
