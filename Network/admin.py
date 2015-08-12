from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from Network.models import IP

class IPAdmin(SingleModelAdmin):
     fieldsets = (
        ('Internet', {
            'fields': ('ip_wan', 'mask_wan', 'gateway', 'dns1', 'dns2')
        }),
        ('Rete Interna', {
            'fields': ('ip_lan', 'mask_lan')
        }),
     )

admin.site.register(IP, IPAdmin)
