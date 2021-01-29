from django.contrib import admin
from .models import Landing


class LandingAdmin(admin.ModelAdmin):
    list_display = ['header_title_1', 'header_content', 'is_published', 'django_content']
    list_editable = ['is_published']


admin.site.register(Landing, LandingAdmin)
