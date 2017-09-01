from django.contrib import messages, admin
from django.conf import settings
from django import forms
from models import WAN, LAN, Management, dhcptable
from singlemodeladmin import SingleModelAdmin
from DashBoard.models import DashBoard
from Proxy.prx_wcf import update_squid
from Proxy.models import Https
from subprocess import call
from License import bf
import os
import iptools
import netifaces
import re


class DeviceWANForm(forms.ModelForm):
    class Meta:
        model = WAN
        widgets = {
            'eth_ip_wan': forms.Select(),
        }
        fields = '__all__'


class DeviceLANForm(forms.ModelForm):
    class Meta:
        model = LAN
        widgets = {
            'eth_ip_lan': forms.Select(),
        }
        fields = '__all__'


class ManagementAdmin(SingleModelAdmin):
    list_display = ('mac',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(ManagementAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(ManagementAdmin, self).add_view(request, form_url, extra_context=extra_context)


class WANAdmin(SingleModelAdmin):
    form = DeviceWANForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        dev_wan = WAN.objects.values()[0]['eth_ip_wan']

        if db_field.name == 'eth_ip_wan':
            kwargs['widget'].choices = (
                (dev_wan, dev_wan),
            )
        return super(WANAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    fieldsets = (
        ('Impostazione WAN', {
            'fields': ('eth_ip_wan', 'ip_wan', 'mask_wan', 'gateway', 'dns1', 'dns2')
            }),)

    def save_model(self, request, obj, form, change):
        ip_wan = form.cleaned_data['ip_wan']
        mask_wan = form.cleaned_data['mask_wan']
        gateway = form.cleaned_data['gateway']
        dns1 = form.cleaned_data['dns1']
        dns2 = form.cleaned_data['dns2']
        if dns1 == dns2:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Gli IP dal DNS non devono essere uguali")
        else:
            if ip_wan == gateway:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "L'IP dal gateway non puo' essere uguale dal IP della WAN")
            else:
                dhcp_range = iptools.IpRange(ip_wan + '/' + mask_wan)
                if gateway in dhcp_range:
                    super(WANAdmin, self).save_model(request, obj, form, change)
                else:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, "Questo gateway non appartiene all'interfaccia WAN.")

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(WANAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(WANAdmin, self).add_view(request, form_url, extra_context=extra_context)


class LANAdmin(admin.ModelAdmin):
    form = DeviceLANForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        dev_lan0 = LAN.objects.all().values()[0]['eth_ip_lan']

        if db_field.name == 'eth_ip_lan':
            kwargs['widget'].choices = (
                (dev_lan0, dev_lan0),
            )
        return super(LANAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    list_display = ('link_on', 'ip_lan', 'mask_lan', 'dhcp', 'ip_start', 'ip_end')

    def link_on(self, request):
        addr = netifaces.ifaddresses(request.eth_ip_lan)
        if netifaces.AF_INET not in addr:
            return u"<font color=\"red\">%s (link down!)</font>" % str(request.eth_ip_lan)
        else:
            return u"<font color=\"green\">%s</font>" % str(request.eth_ip_lan)

    link_on.allow_tags = True
    link_on.short_description = 'Interfaccia'

    fieldsets = (
        ('Impostazione LAN', {
            'fields': ('eth_ip_lan', 'ip_lan', 'mask_lan')
        }),
        ('DHCP Server', {
            'fields': ('dhcp', 'ip_start', 'ip_end')
        }),)

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        remote_addr = request.META['REMOTE_ADDR']
        ip_lan = form.cleaned_data['ip_lan']
        mask_lan = form.cleaned_data['mask_lan']
        dhcp = form.cleaned_data['dhcp']
        ip_start = form.cleaned_data['ip_start']
        ip_end = form.cleaned_data['ip_end']
        iface_range = iptools.IpRange(ip_lan + '/' + mask_lan)
        if dhcp is True:
            if ip_start == ip_lan or ip_end == ip_lan or ip_start == ip_end:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "L'IP dal range non puo' essere uguale dal IP della rete associata")
            else:
                dhcp_range = iptools.IpRange(ip_lan + '/' + mask_lan)
                if ip_start in dhcp_range and ip_end in dhcp_range:
                    if remote_addr not in iface_range:
                        messages.set_level(request, messages.WARNING)
                        messages.warning(request,
                                         "Impostare un IP diverso da dove e' connesso puo' causare perdida di connessione. "
                                         "Ricordi cambiare dopo l'IP per accedere di nuovo.")
                    super(LANAdmin, self).save_model(request, obj, form, change)
                else:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, "Questa network non appartiene all'interfaccia LAN.")
        else:
            obj.ip_start = '0.0.0.0'
            obj.ip_end = '0.0.0.0'
            if remote_addr not in iface_range:
                messages.set_level(request, messages.WARNING)
                messages.warning(request,
                                 "Impostare un IP diverso da dove e' connesso puo' causare perdida di connessione. "
                                 "Ricordi cambiare dopo l'IP per accedere di nuovo.")
            super(LANAdmin, self).save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(LANAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(LANAdmin, self).add_view(request, form_url, extra_context=extra_context)

    def get_actions(self, request):
        try:
            actions = 'delete_selected'
            if request.POST['action'] is None:
                del actions['delete_selected']
                return actions
        except:
            pass


class dhcptableAdmin(admin.ModelAdmin):
    list_display = ('name', 'mac', 'ip')

    def save_model(self, request, obj, form, change):
        ip_check = form.cleaned_data['ip']
        ip_lan = LAN.objects.values()[0]['ip_lan']
        mask_lan = LAN.objects.values()[0]['mask_lan']
        dhcp_range = iptools.IpRange(ip_lan + '/' + mask_lan)
        if str(ip_check) == str(ip_lan):
            messages.set_level(request, messages.ERROR)
            messages.error(request, "L'indirizzo IP e' gia' in utilizzo nella impostazione rete. Prova un'altro.")
        elif ip_check in dhcp_range:
            super(dhcptableAdmin, self).save_model(request, obj, form, change)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "L'indirizzo IP non appartiene alla rete impostata nella voce Networking. Verifiche e provi di nuovo")


class ApplyAdmin(admin.ModelAdmin):
    exclude = ('data_import',)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False

        mac = Management.objects.values()[0]['mac']
        re_mac = re.compile('([a-fA-F0-9]{2}[:|\-]?){6}').search(mac)
        if re_mac is not None:
            pass
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Il campo MAC Management non e' stato aggiunto ancora.")
            return super(ApplyAdmin, self).add_view(request, form_url, extra_context=extra_context)

        eth_ip_wan = WAN.objects.values()[0]['eth_ip_wan']
        eth_ip_lan1 = LAN.objects.values()[0]['eth_ip_lan']
        ip_wan = WAN.objects.values()[0]['ip_wan']
        mask_wan = WAN.objects.values()[0]['mask_wan']
        gateway = WAN.objects.values()[0]['gateway']
        dns1 = WAN.objects.values()[0]['dns1']
        dns2 = WAN.objects.values()[0]['dns2']
        ip_lan = LAN.objects.values()[0]['ip_lan']
        mask_lan = LAN.objects.values()[0]['mask_lan']
        dhcp = LAN.objects.values()[0]['dhcp']
        ip_start = LAN.objects.values()[0]['ip_start']
        ip_end = LAN.objects.values()[0]['ip_end']
        network_conf = open(settings.NETWORK_CONF, 'w')
        parameters = 'auto lo ' + str(eth_ip_wan) + ' ' + str(eth_ip_lan1) + '\n' + \
                     'iface lo inet loopback\n' \
                     'iface ' + str(eth_ip_wan) + ' inet static\n' \
                     '\taddress ' + ip_wan + '\n' \
                     '\tnetwork ' + mask_wan + '\n' \
                     '\tgateway ' + gateway + '\n\n' \
                     '\tdns-nameservers ' + dns1 + ' ' + dns2 + '\n\n' \
                     'iface ' + str(eth_ip_lan1) + ' inet static\n' \
                     '\taddress ' + ip_lan + '\n' \
                     '\tnetwork ' + mask_lan + '\n\n'
        network_conf.write(str(parameters))
        network_conf.close()
        if dhcp is True:
            dhcp_conf = open(settings.DHCP_CONF, 'w')
            parameters = 'ddns-update-style none;\n' \
                         'authoritative;\n' \
                         'option domain-name "aron.proxy.local";\n' \
                         'option domain-name-servers ' + dns1 + ', ' + dns2 + ';\n' \
                         'default-lease-time 28800;\n' \
                         'max-lease-time 28800;\n' \
                         'log-facility local7;\n\n'
            dhcp_conf.write(str(parameters))
            dhcp_conf.close()
            if dhcp is True:
                dhcp_range = iptools.IpRange(ip_lan + '/' + mask_lan)
                n2p = iptools.ipv4.netmask2prefix(mask_lan)
                subnet_lan = iptools.ipv4.cidr2block(ip_lan + '/' + str(n2p))
                if ip_start in dhcp_range and ip_end in dhcp_range:
                    dhcp_conf = open(settings.DHCP_CONF, 'a')
                    parameters_lan_1 = 'subnet ' + subnet_lan[0] + ' netmask ' + mask_lan + ' {\n' \
                                       '\tinterface ' + eth_ip_lan1 + ';\n' \
                                       '\trange ' + ip_start + ' ' + ip_end + ';\n' \
                                       '\toption routers ' + ip_lan + ';\n' \
                                       '}\n'
                    dhcp_conf.write(str(parameters_lan_1))
                    if dhcptable.objects.count() > 0:
                        for i in range(0, dhcptable.objects.count()):
                            fixed_ip = '\nhost ' + str(dhcptable.objects.values()[i]['name']).replace(" ", "_") + ' {\n' \
                                         '\thardware ethernet ' + dhcptable.objects.values()[i]['mac'] + ';\n' \
                                         '\tfixed-address ' + dhcptable.objects.values()[i]['ip'] + ';\n' \
                                         '}\n'
                            dhcp_conf.write(str(fixed_ip))
                    dhcp_conf.close()
            else:
                pass

            aron_server = open(settings.SQUID_DIR + 'aron_server', 'w')
            aron_server.write(ip_lan + '\n')
            aron_server.close()
            aron_dns = open('/etc/resolv.conf', 'w')
            aron_dns.write('nameserver ' + dns1 + '\nnameserver ' + dns2 + '\n')
            aron_dns.close()
            mac_mgmnt = open(settings.FIREHOL_DIR + 'mac_allow', 'w')
            mac_mgmnt.write(mac)
            mac_mgmnt.close()
            try:
                dashboard = DashBoard.objects.get()
                dashboard.wan_image = eth_ip_wan
                dashboard.lan1_image = eth_ip_lan1
                dashboard.save()
                self.mrtg(eth_ip_wan=eth_ip_wan, eth_ip_lan1=eth_ip_lan1, ip_wan=ip_wan, ip_lan1=ip_lan)
            except:
                pass
            call([bf.decrypt('La29TyftnrrorPZ3OtbDs65HKl7UB7q+yofylSaOkVA='), bf.decrypt('8Q2QrJoqMFXIMuqq11YGpox4LId3NDove/OBAlwTvn8='), bf.decrypt('lBII963pDKuc5f61nZ/XOq5HKl7UB7q+yofylSaOkVA=')])
            call([bf.decrypt('La29TyftnrrorPZ3OtbDs65HKl7UB7q+yofylSaOkVA='), bf.decrypt('N6S0ZK5aTP0ehPyDsRqFmJBr1zGF3V62LS4nWPSqXAI='), bf.decrypt('NiBV5Xu1WQKleUQ6h1CWjK5HKl7UB7q+yofylSaOkVA=')])
            call([bf.decrypt('La29TyftnrrorPZ3OtbDs65HKl7UB7q+yofylSaOkVA='), bf.decrypt('k32gcHQPs6nT7ezph/4wJq5HKl7UB7q+yofylSaOkVA='), bf.decrypt('9ha+BbcXydvZS7pQjJHa265HKl7UB7q+yofylSaOkVA='), bf.decrypt('5pmzlN5uhit468pHDJ5trKbR4SPnSsmlwm8cXli//kM=')])
            https = Https.objects.values()[0]['https']
            if https is True:
                update_squid(https=True)
            else:
                update_squid(https=False)

        messages.set_level(request, messages.INFO)
        msg = "Impostazione di rete applicate"
        self.message_user(request, msg, level=messages.INFO)
        return super(ApplyAdmin, self).add_view(request, form_url, extra_context=extra_context)

    def mrtg(self, eth_ip_wan, eth_ip_lan1, ip_wan, ip_lan1):
        call([bf.decrypt('La29TyftnrrorPZ3OtbDs65HKl7UB7q+yofylSaOkVA='), bf.decrypt('I2Zf0k5vpk6oXFUrO79xfq5HKl7UB7q+yofylSaOkVA='), bf.decrypt('DU1G21AJtui6c1472PCYxq5HKl7UB7q+yofylSaOkVA=')])
        mrtg_cfg = 'LoadMIBs: /usr/share/snmp/mibs/UCD-SNMP-MIB.txt\n' \
                   'RunAsDaemon: Yes\n' \
                   'Interval: 5\n' \
                   'WorkDir: ' + settings.STATICFILES_DIRS[0] + '/dashboard/\n' \
                   'Options[_]: growright, bits\n' \
                   'EnableIPv6: no\n\n' \
                   'Target[localhost_' + eth_ip_wan + ']: #' + eth_ip_wan + ':' + settings.SNMP + '@localhost:\n' \
                   'SetEnv[localhost_' + eth_ip_wan + ']: MRTG_INT_IP="' + ip_wan + '" MRTG_INT_DESCR="No-Description"\n' \
                   'MaxBytes[localhost_' + eth_ip_wan + ']: 125000000\n' \
                   'Title[localhost_' + eth_ip_wan + ']: Traffic Analysis for ' + eth_ip_wan + ' -- aron\n\n' \
                   'Target[localhost_' + eth_ip_lan1 + ']: #' + eth_ip_lan1 + ':' + settings.SNMP + '@localhost:\n' \
                   'SetEnv[localhost_' + eth_ip_lan1 + ']: MRTG_INT_IP="' + ip_lan1 + '" MRTG_INT_DESCR="No-Description"\n' \
                   'MaxBytes[localhost_' + eth_ip_lan1 + ']: 125000000\n' \
                   'Title[localhost_' + eth_ip_lan1 + ']: Traffic Analysis for ' + eth_ip_lan1 + ' -- aron\n\n'
        mrtg_file = open('/etc/mrtg.cfg', 'w')
        mrtg_file.write(mrtg_cfg)
        mrtg_file.close()
        call([bf.decrypt('La29TyftnrrorPZ3OtbDs65HKl7UB7q+yofylSaOkVA'), bf.decrypt('5OrsWSLuro/EvB93dMuEp65HKl7UB7q+yofylSaOkVA='), bf.decrypt('gbqllSoikDDSwExVJX0UeK5HKl7UB7q+yofylSaOkVA='), bf.decrypt('78c60PMbJ1mRWp237e0AT65HKl7UB7q+yofylSaOkVA=')])
