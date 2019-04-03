from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User
from user.cms.model_admin import UserAdmin, GroupAdmin


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
