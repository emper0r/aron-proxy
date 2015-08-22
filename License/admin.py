from django.contrib import admin
from django.contrib.auth.admin import User
from django.contrib.auth.admin import Group
from django.contrib import messages
from singlemodeladmin import SingleModelAdmin
from License.models import License
from Posta.models import VeximDomains, VeximUsers
from Posta.admin import VeximDomainAdmin, VeximUserAdmin
from Internet.models import Classi
from Internet.models import IP
from Internet.models import MAC
from Internet.models import WebContentFilter
from Internet.models import Professori
from Internet.models import NewDevices
from Internet.admin import ClassiAdmin, IPAdmin, MACAdmin, WebContentFilterAdmin, NewDevicesAdmin, ProfessoriAdmin
from Network.models import IPNetwork
from Network.admin import IPNetworkAdmin
from web import settings
import os
import time
import urllib2
import bf

class LicAdmin(SingleModelAdmin):
    k = License.objects.all().count()
    if k > 0:
        readonly_fields = ('client', 'province', 'masq_req', 'masq_lic', 'masq_date')
        exclude = ('req', 'lic', 'exp_lic')
    else:
        list_display = ('req', 'lic')
        exclude = ('client', 'province', 'masq_req', 'masq_lic', 'exp_lic')

    def save_model(self, request, obj, form, change):
        k = License.objects.all().count()
        if k is 0:
            response = urllib2.urlopen(settings.SERVER_LIC + 'rl/' + obj.req + '/' + obj.lic, timeout=10)
            server_lic = response.read()
            if server_lic.split()[0] is '0':
                client = server_lic.split()[1]
                province = server_lic.split()[2]
                date = bf.crypt(server_lic.split()[3])
                req = bf.crypt(obj.req)
                lic = bf.crypt(obj.lic)
                License.objects.create(client=client, province=province, req=req, lic=lic, exp_lic=date)
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
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Licenza e gia' attiva.")

if License.objects.all().count() is 0:
    admin.site.unregister(User)
    admin.site.unregister(Group)

admin.site.register(License, LicAdmin)
admin.site.register(IPNetwork, IPNetworkAdmin)

if License.objects.all().count() > 0:
    admin.site.register(Classi, ClassiAdmin)
    admin.site.register(IP, IPAdmin)
    admin.site.register(MAC, MACAdmin)
    admin.site.register(WebContentFilter, WebContentFilterAdmin)
    admin.site.register(Professori, ProfessoriAdmin)
    admin.site.register(NewDevices, NewDevicesAdmin)
    admin.site.register(VeximDomains, VeximDomainAdmin)
    admin.site.register(VeximUsers, VeximUserAdmin)
