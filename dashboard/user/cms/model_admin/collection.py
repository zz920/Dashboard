from common.cms.model_admin.base import BaseModelAdmin
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.contrib import admin
from django.db.models import Max, Sum, Q, Value, Count
from django.db.models.functions import Coalesce
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import gettext_lazy as _

from common.cms.mixin.view_only import ViewOnlyMixin


class UserCollectionChangeList(ChangeList):
   
    def get_queryset(self, request, **kwargs):
        qs = super().get_queryset(request, **kwargs) 
        return qs.filter(user=request.user)


class UserCollection(BaseModelAdmin):
    list_display = () 

    def get_changelist(self, request, **kwargs):
        return UserCollectionChangeList
