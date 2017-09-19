from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
from django.contrib import admin, messages
from django.contrib.auth.admin import User, Group
from singlemodeladmin import SingleModelAdmin
from License.models import License
from Proxy.models import Classi, MAC, Professori, NewDevices, Blacklist, Https
from Proxy.admin import ClassiAdmin, MACAdmin, NewDevicesAdmin, ProfessoriAdmin, BlacklistAdmin, HttpsAdmin
from Network.models import WAN, LAN, Management, Apply, dhcptable
from Network.admin import WANAdmin, LANAdmin, ManagementAdmin, ApplyAdmin, dhcptableAdmin
from Routing.models import Routing
from Routing.admin import RoutingAdmin
from Configurazione.models import ImportConfig, ExportConfig
from Configurazione.admin import ImportConfigAdmin, ExportConfigAdmin
from DashBoard.models import DashBoard, AronLogs, Top, Cache, Aiuto, LFD
from DashBoard.admin import DashBoardAdmin, AronLogsAdmin, TopAdmin, CacheAdmin, AiutoAdmin, LFDAdmin
from web import settings
from subprocess import call
import os
import time
import urllib2
import bf
import key
import subprocess
import hashlib
import threading
import datetime
import gzip


def cl():
    threading.Timer(1200.0, cl).start()
    temporizer = datetime.datetime.today()
    act_lic = License.objects.all().count()
    if act_lic > 0:
        if temporizer.hour >= 23 and temporizer.minute >= 1 or temporizer.minute <= 59 is True:
            uniq_file = '/tmp/._'
            uniq_id = open(uniq_file, 'w')
            hardware = subprocess.Popen('sudo lspci', shell=True, stdout=subprocess.PIPE)
            for line in hardware.stdout:
                uniq_id.write(line)
            hd = subprocess.Popen('sudo hdparm -i /dev/sda', shell=True, stdout=subprocess.PIPE)
            for line in hd.stdout:
                uniq_id.write(line)
            ethernet = subprocess.Popen('sudo ifconfig | egrep -i ether | awk \'{print $2}\'', shell=True, stdout=subprocess.PIPE)
            for line in ethernet.stdout:
                uniq_id.write(line)
            uniq_id.close()
            with open(uniq_file, 'r') as file_to_check:
                data = file_to_check.read()
                server_id = hashlib.md5(data).hexdigest()
            os.system('rm -f %s' % uniq_file)
            try:
                response = urllib2.urlopen(settings.SERVER_LIC + '/cl/' + server_id, timeout=10)
                server_lic = response.read()
                if int(str(server_lic)[0]) is 0:
                    return
                else:
                    wan = WAN.objects.all().values()[0]['eth_ip_wan']
                    lan1 = LAN.objects.all().values()[0]['eth_ip_lan']
                    mitm = Https.objects.get(pk=1)
                    mitm.https = False
                    mitm.save()
                    proxy_conf = open(settings.SQUID_CONF, 'w')
                    squid_conf = 'http_port 3128 intercept\n' \
                                 'acl localnet src 192.168.0.0/16 172.16.0.0/12 10.0.0.0/8\n' \
                                 'acl localnet src fc00::/7\n' \
                                 'acl localnet src fe80::/10\n' \
                                 'acl SSL_ports port 443\n' \
                                 'acl Safe_ports port 80\n' \
                                 'acl Safe_ports port 21\n' \
                                 'acl Safe_ports port 443\n' \
                                 'acl Safe_ports port 70\n' \
                                 'acl Safe_ports port 210\n' \
                                 'acl Safe_ports port 1025-65535\n' \
                                 'acl Safe_ports port 280\n' \
                                 'acl Safe_ports port 488\n' \
                                 'acl Safe_ports port 591\n' \
                                 'acl Safe_ports port 777\n' \
                                 'acl CONNECT method CONNECT\n' \
                                 'http_access allow localnet\n' \
                                 'http_access deny all\n' \
                                 'negative_ttl 5 minutes\n' \
                                 'positive_dns_ttl 15 hours\n' \
                                 'negative_dns_ttl 1 minutes\n' \
                                 'shutdown_lifetime 1\n' \
                                 'cache_mgr no-reply@aron.proxy.it\n' \
                                 'visible_hostname Aron-Proxy\n' \
                                 'dns_nameservers 8.8.8.8 8.8.4.4\n' \
                                 'access_log none\n'
                    fw = open(settings.FIREHOL_DIR + 'firehol.conf', 'w')
                    fw_conf = 'version 6\n' \
                                  'LAN="10.0.0.0/8 172.16.0.0/16 192.168.0.0/16"\n\n' \
                                  'ipv4 transparent_proxy 80 3128 "root proxy" inface ' + lan1 + '\n\n' \
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
                                  '    route4 all accept\n\n'
                    mode = Routing.objects.get(pk=1)
                    if bf.decrypt(mode.mode) == "Proxy/Classes":
                        mode.mode = bf.crypt("Routing")
                        mode.save()
                    else:
                        pass
                    proxy_conf.write(squid_conf)
                    proxy_conf.close()
                    fw.write(fw_conf)
                    fw.close()
                    os.system("sudo firehol restart")
                    os.system("sudo /etc/init.d/squid restart")
                    l = License.objects.get()
                    l.delete()
                    time.sleep(4)
                    os.system('sudo /etc/init.d/apache2 reload')
                    file_save = open(settings.SQUID_CONF + '.aron', 'wb')
                    file_save.write(bf.crypt(open(settings.SQUID_CONF, 'r').read()))
                    file_save.close()
                    os.remove(settings.SQUID_CONF)
            except:
                return
        else:
            return
    else:
        return

cl()


@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': context.get('show_save_and_add_another', ctx['show_save_and_add_another']),
        'show_save_and_continue': context.get('show_save_and_continue', ctx['show_save_and_continue']),
        'show_save': context.get('show_save', ctx['show_save']),
        'show_save_as_new': context.get('show_save_as_new', ctx['show_save_as_new']),
        'show_delete_link': context.get('show_save_and_add_another', ctx['show_delete_link']),
        })
    return ctx


class LicAdmin(SingleModelAdmin):
    k = License.objects.all().count()
    if k > 0:
        readonly_fields = ('client', 'name', 'masq_qty_dev', 'masq_req', 'masq_lic', 'masq_date')
        exclude = ('req', 'lic', 'exp_lic', 'province', 'qty_dev')
    else:
        list_display = ('req', 'lic')
        exclude = ('client', 'name', 'province', 'qty_dev', 'masq_qty_dev', 'masq_req', 'masq_lic', 'exp_lic')

    def save_model(self, request, obj, form, change):
        k = License.objects.all().count()
        if k is 0:
            try:
                uniq_file = '/tmp/._'
                uniq_id = open(uniq_file, 'w')
                hardware = subprocess.Popen('sudo lspci', shell=True, stdout=subprocess.PIPE)
                for line in hardware.stdout:
                    uniq_id.write(line)
                hd = subprocess.Popen('sudo hdparm -i /dev/sda', shell=True, stdout=subprocess.PIPE)
                for line in hd.stdout:
                    uniq_id.write(line)
                ethernet = subprocess.Popen('sudo ifconfig | egrep -i ether | awk \'{print $2}\'', shell=True, stdout=subprocess.PIPE)
                for line in ethernet.stdout:
                    uniq_id.write(line)
                uniq_id.close()
                with open(uniq_file, 'r') as file_to_check:
                    data = file_to_check.read()
                    server_id = hashlib.md5(data).hexdigest()
                os.system('rm -f %s' % uniq_file)
                response = urllib2.urlopen(settings.SERVER_LIC + '/rl/' + obj.req + '/' + obj.lic + '/' +
                                           bf.crypt(settings.DATABASES.values()[0]['PASSWORD']) + '/' +
                                           server_id, timeout=10)
                server_lic = response.read()
                if int(str(server_lic)[0]) is 0:
                    obj.client = map(str.strip, server_lic.split(','))[1]
                    obj.name = map(str.strip, server_lic.split(','))[2]
                    obj.exp_lic = bf.crypt(map(str.strip, server_lic.split(','))[3][:10])
                    obj.qty_dev = bf.crypt(map(str.strip, server_lic.split(','))[4])
                    obj.req = bf.crypt(obj.req)
                    obj.lic = bf.crypt(obj.lic)
                    messages.set_level(request, messages.SUCCESS)
                    super(LicAdmin, self).save_model(request, obj, form, change)
                    time.sleep(2)
                    os.system('sudo /etc/init.d/apache2 reload')
                    if not os.path.isfile(str(settings.STATICFILES_DIRS[0] + '/' + 'config.aron.factory.prx')):
                        tmp_sql = '/tmp/._.sql'
                        os.system('mysqldump -u %s -h %s --password=%s %s --ignore-table=%s.aron_logs > %s' %
                                  (settings.DATABASES.values()[0]['USER'],
                                   settings.DATABASES.values()[0]['HOST'],
                                   settings.DATABASES.values()[0]['PASSWORD'],
                                   settings.DATABASES.values()[0]['NAME'],
                                   settings.DATABASES.values()[0]['NAME'],
                                   tmp_sql))
                        file_save = gzip.open('/tmp/config.aron.factory.prx', 'wb')
                        file_save.write(bf.crypt(open(tmp_sql, 'r').read()))
                        file_save.close()
                        os.unlink(tmp_sql)
                        os.system("sudo mv /tmp/config.aron.factory.prx %s/" % settings.STATICFILES_DIRS)
                    time.sleep(2)
                    return
                if int(str(server_lic)[0]) is 1:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, "Questa licenza non e' valida, e' necessario richiedere una nuova a Computer Time s.r.l")
                if int(str(server_lic)[0]) is 2:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, "E' gia' stata attivata questa licenza, e' necessario richiedere una nuova a Computer Time s.r.l")
            except:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Questa licenza non e' valida, e' necessario richiedere una nuova a Computer Time s.r.l")
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Licenza e gia' attiva.")

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(LicAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(LicAdmin, self).add_view(request, form_url, extra_context=extra_context)

admin.site.register(License, LicAdmin)
admin.site.register(WAN, WANAdmin)
admin.site.register(LAN, LANAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(dhcptable, dhcptableAdmin)
admin.site.register(Routing, RoutingAdmin)
admin.site.register(ImportConfig, ImportConfigAdmin)
admin.site.register(ExportConfig, ExportConfigAdmin)
admin.site.register(DashBoard, DashBoardAdmin)
admin.site.register(Aiuto, AiutoAdmin)
admin.site.register(LFD, LFDAdmin)
admin.site.register(Top, TopAdmin)
admin.site.register(AronLogs, AronLogsAdmin)


if License.objects.all().count() is 0:
    admin.site.unregister(User)
    admin.site.unregister(Group)
    admin.site.unregister(Routing)
    admin.site.unregister(ImportConfig)
    admin.site.unregister(ExportConfig)
    admin.site.unregister(DashBoard)
    admin.site.unregister(Aiuto)
    admin.site.unregister(LFD)
    admin.site.unregister(Top)
    admin.site.unregister(AronLogs)

if License.objects.all().count() > 0:
    obj = License.objects.get()
    try:
        if str(Routing.objects.values()[0]['mode']) == 'Routing':
            admin.site.unregister(Classi)
            admin.site.unregister(MAC)
            admin.site.unregister(Professori)
            admin.site.unregister(NewDevices)
            admin.site.unregister(Cache)
            admin.site.unregister(Https)
            admin.site.unregister(Blacklist)
        else:
            admin.site.register(Classi, ClassiAdmin)
            admin.site.register(MAC, MACAdmin)
            admin.site.register(Professori, ProfessoriAdmin)
            admin.site.register(Cache, CacheAdmin)
            admin.site.register(NewDevices, NewDevicesAdmin)
            admin.site.register(Blacklist, BlacklistAdmin)
            admin.site.register(Https, HttpsAdmin)
    except:
        pass
