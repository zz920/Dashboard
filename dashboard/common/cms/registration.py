from django.contrib import admin

from common.cms.model_admin import NewsModelAdmin
from common.models import News


admin.site.register(News, NewsModelAdmin)
