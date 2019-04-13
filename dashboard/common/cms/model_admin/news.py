from django.contrib import admin


class NewsModelAdmin(admin.ModelAdmin):

    readonly_fields = ('created_at', 'updated_at', 'updated_by')
