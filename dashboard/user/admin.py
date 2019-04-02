from django.contrib import admin

from user.models import User
from user.cms.model_admin import UserAdmin


admin.site.register(User, UserAdmin)
