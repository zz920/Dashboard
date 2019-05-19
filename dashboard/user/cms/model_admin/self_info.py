from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.http import HttpResponseRedirect
from common.cms.model_admin.base import BaseModelAdmin
from common.cms.mixin.view_only import ViewOnlyMixin


class UserSelfInfoModelAdmin(ViewOnlyMixin, BaseModelAdmin):
    
    fields = ('user_name', 'change_password', 'client_name')
    readonly_fields = ('user_name', 'change_password', 'client_name')
    exclude = ['created_at', 'updated_at', 'updated_by']

    def changelist_view(self, request, extra_content=None):
        url = "{}{}/change".format(reverse('admin:user_userselfinfoproxy_changelist'), request.user.id) 
        return HttpResponseRedirect(url)
    
    def has_view_permission(self, request, obj=None):
        return request.user == obj
    
    def has_change_permission(self, request, obj=None):
        return request.user == obj
