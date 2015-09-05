from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
from django.contrib import admin, messages
from django.contrib.auth.admin import User, Group
from singlemodeladmin import SingleModelAdmin
from License.models import License
from Posta.models import VeximDomains, VeximUsers
from Posta.admin import VeximDomainAdmin, VeximUserAdmin
from Internet.models import Classi, IP, MAC, WebContentFilter, Professori, NewDevices
from Internet.admin import ClassiAdmin, IPAdmin, MACAdmin, WebContentFilterAdmin, NewDevicesAdmin, ProfessoriAdmin
from Network.models import IPNetwork
from Network.admin import IPNetworkAdmin
from web import settings
import os
import time
import urllib2
import bf
import key
import subprocess
import hashlib
import threading

def cl():
    threading.Timer(3600.0, cl).start()
    act_lic = License.objects.all().count()
    if act_lic > 0:
        uniq_file = '/tmp/._'
        uniq_id = open(uniq_file, 'w')
        hardware = subprocess.Popen('sudo lspci', shell=True, stdout=subprocess.PIPE)
        for line in hardware.stdout:
            uniq_id.write(line)
        hd = subprocess.Popen('sudo hdparm -i /dev/sda', shell=True, stdout=subprocess.PIPE)
        for line in hd.stdout:
            uniq_id.write(line)
        ethernet = subprocess.Popen('sudo ifconfig | egrep -i HWaddr | awk \'{print $5}\'', shell=True, stdout=subprocess.PIPE)
        for line in ethernet.stdout:
            uniq_id.write(line)
        uniq_id.close()
        with open(uniq_file, 'r') as file_to_check:
            data = file_to_check.read()
            server_id = hashlib.md5(data).hexdigest()
        # os.system('rm -f %s' % uniq_file)
        response = urllib2.urlopen(settings.SERVER_LIC + 'cl/' + server_id, timeout=10)
        server_lic = response.read()
        if server_lic[0] is '0':
            return
        else:
            l = License.objects.get()
            l.delete()
            time.sleep(4)
            os.system('sudo /etc/init.d/apache2 reload')
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
        readonly_fields = ('client', 'name', 'province', 'masq_req', 'masq_lic', 'masq_date')
        exclude = ('req', 'lic', 'exp_lic')
    else:
        list_display = ('req', 'lic')
        exclude = ('client', 'name', 'province', 'masq_req', 'masq_lic', 'exp_lic')

    def save_model(self, request, obj, form, change):
        k = License.objects.all().count()
        if k is 0:
            try:
                assert key.validate(obj.req, obj.lic) is 0
                uniq_file = '/tmp/._'
                uniq_id = open(uniq_file, 'w')
                hardware = subprocess.Popen('sudo lspci', shell=True, stdout=subprocess.PIPE)
                for line in hardware.stdout:
                    uniq_id.write(line)
                hd = subprocess.Popen('sudo hdparm -i /dev/sda', shell=True, stdout=subprocess.PIPE)
                for line in hd.stdout:
                    uniq_id.write(line)
                ethernet = subprocess.Popen('sudo ifconfig | egrep -i HWaddr | awk \'{print $5}\'', shell=True, stdout=subprocess.PIPE)
                for line in ethernet.stdout:
                    uniq_id.write(line)
                uniq_id.close()
                with open(uniq_file, 'r') as file_to_check:
                    data = file_to_check.read()
                    server_id = hashlib.md5(data).hexdigest()
                # os.system('rm -f %s' % uniq_file)
                response = urllib2.urlopen(settings.SERVER_LIC + 'rl/' + obj.req + '/' + obj.lic + '/' + server_id, timeout=10)
                server_lic = response.read()
                if server_lic[0] is '0':
                    obj.client = map(str.strip, server_lic.split(','))[1]
                    obj.name = map(str.strip, server_lic.split(','))[2]
                    obj.province = map(str.strip, server_lic.split(','))[3]
                    obj.exp_lic = bf.crypt(map(str.strip, server_lic.split(','))[4][:10])
                    key.validate(obj.req, obj.lic)
                    obj.req = bf.crypt(obj.req)
                    obj.lic = bf.crypt(obj.lic)
                    super(LicAdmin, self).save_model(request, obj, form, change)
                    messages.set_level(request, messages.SUCCESS)
                    time.sleep(4)
                    os.system('sudo /etc/init.d/apache2 reload')
                if server_lic[0] is '1':
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, "Questa licenza non e' valida, e' necessario richiedere una nuova a Computer Time s.r.l")
                if server_lic[0] is '2':
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
        return super(LicAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(LicAdmin, self).add_view(request, form_url, extra_context=extra_context)

if License.objects.all().count() is 0:
    admin.site.unregister(User)
    admin.site.unregister(Group)

admin.site.register(License, LicAdmin)
admin.site.register(IPNetwork, IPNetworkAdmin)

if License.objects.all().count() > 0:
    try:
        obj = License.objects.get()
        assert key.validate(bf.decrypt(obj.req), bf.decrypt(obj.lic)) is 0
        admin.site.register(Classi, ClassiAdmin)
        admin.site.register(IP, IPAdmin)
        admin.site.register(MAC, MACAdmin)
        admin.site.register(WebContentFilter, WebContentFilterAdmin)
        admin.site.register(Professori, ProfessoriAdmin)
        admin.site.register(NewDevices, NewDevicesAdmin)
        admin.site.register(VeximDomains, VeximDomainAdmin)
        admin.site.register(VeximUsers, VeximUserAdmin)
    except:
        admin.site.unregister(User)
        admin.site.unregister(Group)
