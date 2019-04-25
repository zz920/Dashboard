from django.contrib.admin.sites import DefaultAdminSite
from django.contrib.admin.apps import AdminConfig
from django.http import HttpResponseRedirect


class DashboardAdminSite(DefaultAdminSite):

    def app_index(self, request, app_label, extra_context=None):
        if not request.user.is_superuser:
            return HttpResponseRedirect('/')
        return super(DashboardAdminSite, self).app_index(request, app_label, extra_context)


class DashboardAdminConfig(AdminConfig):
    default_site = DashboardAdminSite
