from singlemodeladmin import SingleModelAdmin
from web import settings
import os
from django.contrib import admin, messages
from django.contrib.auth.admin import User, Group
from Proxy.models import Classi, MAC, Professori, NewDevices, Https, Blacklist
from Proxy.admin import ClassiAdmin, MACAdmin, NewDevicesAdmin, ProfessoriAdmin, HttpsAdmin, BlacklistAdmin
from Proxy.prx_wcf import update_squid
from Network.models import WAN, LAN, Management
from Routing.models import Routing
from License import bf
import re


class RoutingAdmin(SingleModelAdmin):
    fieldsets = (
        ('Funzionalita\'', {
            'fields': ('mode', )
            }),
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(RoutingAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        mac = Management.objects.values()[0]['mac']
        if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
            mode = form.cleaned_data['mode']
            wan = WAN.objects.all().values()[0]['eth_ip_wan']
            lan1 = LAN.objects.all().values()[0]['eth_ip_lan']
            if mode == 'Routing':
                mitm = Https.objects.get(pk=1)
                mitm.https = False
                mitm.save()
                admin.site.unregister(Classi)
                admin.site.unregister(MAC)
                admin.site.unregister(Professori)
                admin.site.unregister(NewDevices)
                admin.site.unregister(Https)
                admin.site.unregister(Blacklist)
                admin.site.unregister(User)
                admin.site.unregister(Group)
                fw = open(settings.FIREHOL_DIR + 'firehol.conf', 'w')
                fw_conf = 'version 6\n' \
                          'LAN="10.0.0.0/8 172.16.0.0/16 192.168.0.0/16"\n\n' \
                          'ipv4 transparent_proxy 80 3128 "root proxy" inface ' + lan1 + '\n' \
                          'FIREHOL_LOG_LEVEL=7\n' \
                          'interface4 ' + wan + ' ethernet\n' \
                          '    UNMATCHED_INPUT_POLICY=DROP\n' \
                          '    UNMATCHED_OUTPUT_POLICY=DROP\n' \
                          '    UNMATCHED_FORWARD_POLICY=DROP\n' \
                          '    FIREHOL_LOG_FREQUENCY="1/second"\n' \
                          '    FIREHOL_LOG_BURST="1"\n' \
                          '    policy drop\n' \
                          '    ipv4 server "icmp ssh" accept\n' \
                          '    ipv4 client all accept\n\n' \
                          'interface4 ' + lan1 + ' lan1 src "${LAN}"\n' \
                          '    policy accept\n' \
                          '    ipv4 server all accept\n' \
                          '    ipv4 client all accept\n\n' \
                          'router4 lan-1-inet inface ' + lan1 + ' outface ' + wan + '\n' \
                          '    masquerade\n' \
                          '    route4 all accept\n'
                fw.write(str(fw_conf))
                fw.close()
                update_squid(https=False)
                os.system("sudo firehol restart")

            if mode == 'Proxy/Classes':
                admin.site.register(User)
                admin.site.register(Group)
                admin.site.register(Classi, ClassiAdmin)
                admin.site.register(MAC, MACAdmin)
                admin.site.register(Professori, ProfessoriAdmin)
                admin.site.register(NewDevices, NewDevicesAdmin)
                admin.site.register(Https, HttpsAdmin)
                admin.site.register(Blacklist, BlacklistAdmin)
                fw = open(settings.FIREHOL_DIR + 'firehol.conf', 'w')
                fw_conf = 'version 6\n' \
                          'LAN="10.0.0.0/8 172.16.0.0/16 192.168.0.0/16"\n\n' \
                          'MAC_ALLOW="`cat /etc/firehol/mac_allow`"\n' \
                          'ipv4 redirect to 8888 proto tcp dport 80 dst not "${UNROUTABLE_IPS}" mac not "${MAC_ALLOW}" log "REDIRECTING 80 TO 8888"\n' \
                          'ipv4 redirect to 8888 proto tcp dport 443 dst not "${UNROUTABLE_IPS}" mac not "${MAC_ALLOW}" log "REDIRECTING 443 TO 8888"\n' \
                          'ipv4 transparent_proxy 80 3128 "root proxy" inface ' + lan1 + '\n' \
                          'FIREHOL_LOG_LEVEL=7\n' \
                          'interface4 ' + wan + ' ethernet\n' \
                          '    UNMATCHED_INPUT_POLICY=DROP\n' \
                          '    UNMATCHED_OUTPUT_POLICY=DROP\n' \
                          '    UNMATCHED_FORWARD_POLICY=DROP\n' \
                          '    FIREHOL_LOG_FREQUENCY="1/second"\n' \
                          '    FIREHOL_LOG_BURST="1"\n' \
                          '    policy drop\n' \
                          '    ipv4 server "icmp ssh" accept\n' \
                          '    ipv4 client all accept\n\n' \
                          'interface4 ' + lan1 + ' lan1 src "${LAN}"\n' \
                          '    UNMATCHED_INPUT_POLICY=DROP\n' \
                          '    UNMATCHED_OUTPUT_POLICY=DROP\n' \
                          '    UNMATCHED_FORWARD_POLICY=DROP\n' \
                          '    FIREHOL_LOG_FREQUENCY="1/second"\n' \
                          '    FIREHOL_LOG_BURST="1"\n' \
                          '    policy drop\n' \
                          '    ipv4 server "icmp ssh dhcp squid dns" accept src "${LAN}"\n' \
                          '    ipv4 server custom aron-t tcp/8088 default accept src "${LAN}"\n' \
                          '    ipv4 server custom prx-t tcp/3129 default accept src "${LAN}"\n' \
                          '    ipv4 client all accept\n\n' \
                          'router4 lan-1-inet inface ' + lan1 + ' outface ' + wan + '\n' \
                          '    masquerade\n' \
                          '    route4 all accept mac "${MAC_ALLOW}"\n'
                fw.write(str(fw_conf))
                fw.close()
                os.system("sudo firehol restart")
                update_squid(https=False)
            obj.mode = bf.crypt(mode)
            super(RoutingAdmin, self).save_model(request, obj, form, change)
            messages.set_level(request, messages.SUCCESS)
        else:
            mode = Routing.objects.values()[0]['mode']
            obj.mode = bf.crypt(mode)
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Devi inserire un MAC valido in Network / MAC Management prima di cambiare il modo.")
