from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at', 'updated_by']
