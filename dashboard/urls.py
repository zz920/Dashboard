from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from rest_framework import renderers

from conf import settings
from dashboard_celery import app


urlpatterns = [
                    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
                    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                    path('', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Panda Dashboard"
admin.site.site_title = "Panda Dashboard"
admin.site.index_title = "Welcome to Panda Dashboard"
