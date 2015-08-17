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
import os
import key

admin.site.unregister(User)
admin.site.unregister(Group)

class LicAdmin(SingleModelAdmin):
    k = License.objects.all().count()
    if k > 0:
        readonly_fields = ('client', 'province', 'lic', 'req', 'exp_lic')
    else:
        list_display = ('lic', 'req')
        exclude = ('exp_lic',)

    def save_model(self, request, obj, form, change):
        k = License.objects.all().count()
        if k is 0:
            lic = form.cleaned_data['lic']
            req = form.cleaned_data['req']
            check_lic = key.validate(req, lic)
            if check_lic is 0:
                super(LicAdmin, self).save_model(request, obj, form, change)
                messages.set_level(request, messages.SUCCESS)
                messages.error(request, "Devi uscire ed entrare nel sistema di nuovo.")
                os.system("/etc/init.d/apache2 restart")
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Licenza invalida, chiede assistenza a Computer Time s.r.l")
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Licenza e gia' attivata.")

admin.site.register(License, LicAdmin)
if License.objects.all().count() > 0:
    admin.site.register(User)
    admin.site.register(Group)
    admin.site.register(Classi, ClassiAdmin)
    admin.site.register(IP, IPAdmin)
    admin.site.register(MAC, MACAdmin)
    admin.site.register(WebContentFilter, WebContentFilterAdmin)
    admin.site.register(Professori, ProfessoriAdmin)
    admin.site.register(NewDevices, NewDevicesAdmin)
    admin.site.register(IPNetwork, IPNetworkAdmin)
    admin.site.register(VeximDomains, VeximDomainAdmin)
    admin.site.register(VeximUsers, VeximUserAdmin)
