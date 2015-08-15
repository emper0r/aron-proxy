from django.contrib import admin
from django.contrib import messages
from singlemodeladmin import SingleModelAdmin
from Network.models import IP
import iptools


class IPAdmin(SingleModelAdmin):
    fieldsets = (
        ('Internet', {
            'fields': ('ip_wan', 'mask_wan', 'gateway', 'dns1', 'dns2')
            }),
        ('Rete Interna', {
            'fields': ('ip_lan', 'mask_lan')
            }),
        ('DHCP', {
            'fields': ('dhcp', 'ip_start', 'ip_end')
            }),
    )

    def save_model(self, request, obj, form, change):
        ip_lan = form.cleaned_data['ip_lan']
        mask_lan = form.cleaned_data['mask_lan']
        ip_start = form.cleaned_data['ip_start']
        ip_end = form.cleaned_data['ip_end']
        dhcp_range = iptools.IpRange(ip_lan + '/' + mask_lan)
        if ip_start in dhcp_range and ip_end in dhcp_range:
            super(IPAdmin, self).save_model(request, obj, form, change)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Questo rango non apartiene all'interfaccia LAN.")

admin.site.register(IP, IPAdmin)
