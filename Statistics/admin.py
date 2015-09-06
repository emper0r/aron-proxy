from django.contrib import admin
from django.conf.urls import patterns
from Statistics import views

class SquidLogsAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(SquidLogsAdmin, self).get_urls()
        my_urls = patterns('',
                           (r'^$', views.statistics)
        )
        return my_urls + urls
