from common.cms.model_admin.base import BaseModelAdmin

from user.cms.model_admin.inline import CustomerInline

class UserAdmin(BaseModelAdmin):
    inlines = (CustomerInline, )
