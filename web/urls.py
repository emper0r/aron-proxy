from django.conf.urls import patterns, include, url
from django.contrib import admin
from Statistics import views

admin.site.site_header = 'Aron Web Manager'

urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
    url(r'^statistics$', views.statistics, name='top_ten'),
)
