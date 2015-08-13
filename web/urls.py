from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'Aron Web Manager'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include(frontend_urls)),
)
