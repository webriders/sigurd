# -*- coding: UTF-8 -*-
from django.contrib import admin
from web.models import Application, ApplicationConfig, DownloadItem


class ApplicationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('slug', 'url', 'published',)
    list_editable = ('published',)


class ApplicationConfigAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'application', 'slug', 'downloads', 'published', 'is_master',)
    list_editable = ('published',)


class DownloadItemAdmin(admin.ModelAdmin):
    save_on_top = True

admin.site.register(DownloadItem, DownloadItemAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationConfig, ApplicationConfigAdmin)
