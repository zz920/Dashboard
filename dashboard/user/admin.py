from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User, Role, Access
from user.cms.model_admin import UserAdmin, RoleAdmin, AccessAdmin


#admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Access, AccessAdmin)
