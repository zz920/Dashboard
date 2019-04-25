from django.contrib.admin.apps import AdminConfig


class DashboardAdminConfig(AdminConfig):
    default_site = 'common.admin.DashboardAdminSite'
