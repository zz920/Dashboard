from django.conf.urls.static import static
from django.utils.translation import gettext as _
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from rest_framework import renderers

from conf import settings


urlpatterns = [
                    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
                    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                    # re_path(r'^accounts/', include('registration.backends.default.urls')),
                    path('', admin.site.urls),
                    path('task-rq/', include('django_rq_dashboard.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = _("Panda Dashboard")
admin.site.site_title = _("Panda Dashboard")
admin.site.index_title = _("Welcome to Panda Dashboard")
