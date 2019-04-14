from django.contrib import admin


class NewsModelAdmin(admin.ModelAdmin):

    exclude = ('created_at', 'updated_at', 'updated_by')
    readonly_fields = ('html_content',)
