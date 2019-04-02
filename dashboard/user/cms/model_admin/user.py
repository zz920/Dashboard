from django.contrib import admin

from user.cms.model_admin.inline import CustomerInline

class UserAdmin(admin.ModelAdmin):
    inlines = (CustomerInline, )
