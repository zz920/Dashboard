from django.contrib.auth.admin import GroupAdmin as Admin

from common.cms.model_admin import BaseModelAdmin


class GroupAdmin(Admin, BaseModelAdmin):
    pass
