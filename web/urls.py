from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'Aron Web Manager'

urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
)
