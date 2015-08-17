from django.contrib import messages
from django.conf import settings
from singlemodeladmin import SingleModelAdmin
from Network.models import IPNetwork
import os
import iptools


class IPNetworkAdmin(SingleModelAdmin):
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
        ip_wan = form.cleaned_data['ip_wan']
        mask_wan = form.cleaned_data['mask_wan']
        gateway = form.cleaned_data['gateway']
        ip_lan = form.cleaned_data['ip_lan']
        mask_lan = form.cleaned_data['mask_lan']
        ip_start = form.cleaned_data['ip_start']
        ip_end = form.cleaned_data['ip_end']
        dns1 = form.cleaned_data['dns1']
        dns2 = form.cleaned_data['dns2']
        dhcp_range = iptools.IpRange(ip_wan + '/' + mask_wan)
        if gateway in dhcp_range:
            network_conf = open(settings.NETWORK_CONF, 'w')
            parameters = 'auto lo eth0 eth1\n' \
                         'iface lo inet loopback\n' \
                         'iface eth0 inet static\n' \
                         '\taddress ' + ip_wan + '\n' \
                         '\tnetwork ' + mask_wan + '\n' \
                         '\tgateway ' + gateway + '\n\n' \
                         '\tdns-servers ' + dns1 + ' ' + dns2 + '\n\n' \
                         'iface eth1 inet static\n' \
                         '\taddress ' + ip_lan + '\n' \
                         '\tnetwork ' + mask_lan + '\n'
            network_conf.write(str(parameters))
            network_conf.close()
            os.system("/etc/network/interfaces restart")
            dhcp_range = iptools.IpRange(ip_lan + '/' + mask_lan)
            if ip_start in dhcp_range and ip_end in dhcp_range:
                dhcp_conf = open(settings.DHCP_CONF, 'w')
                parameters = 'ddns-update-style none;\n' \
                             'authoritative;\n' \
                             'option domain-name "aron.local";\n' \
                             'option domain-name-servers ' + dns1 +', ' + dns2 + ';\n' \
                             'default-lease-time 600;\n' \
                             'max-lease-time 7200;\n' \
                             'log-facility local7;\n\n' \
                             'subnet ' + ip_lan + ' netmask ' + mask_lan + ' { \n' \
                             '\trange ' + ip_start + ' ' + ip_end + ';\n' \
                             '\toption routers ' + ip_lan + ';\n' \
                             '}\n'
                dhcp_conf.write(str(parameters))
                dhcp_conf.close()
                self.dhcp_run()
                super(IPNetworkAdmin, self).save_model(request, obj, form, change)
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Questo rango non apartiene all'interfaccia LAN.")
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Il gateway e' sbagliato.")

    def dhcp_run(self):
        service = IPNetwork.objects.all()
        if service.values()[0]['dhcp'] is True:
            os.system('/etc/init.d/isc-dhcp-server restart')
        else:
            os.system('/etc/init.d/isc-dhcp-server stop')
