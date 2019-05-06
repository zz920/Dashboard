from django.contrib import admin
from django.http import HttpResponseRedirect


class DashboardAdminSite(admin.AdminSite):

    def app_index(self, request, app_label, extra_context=None):
        if not request.user.is_superuser:
            return HttpResponseRedirect('/')
        return super(DashboardAdminSite, self).app_index(request, app_label, extra_context)
