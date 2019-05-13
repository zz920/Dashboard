from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User, UserSelfInfoProxy
from user.cms.model_admin import UserModelAdmin, GroupAdmin, UserSelfInfoModelAdmin


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserModelAdmin)
admin.site.register(UserSelfInfoProxy, UserSelfInfoModelAdmin)
