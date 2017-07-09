from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
from django.contrib import admin, messages
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.conf import settings
from singlemodeladmin import SingleModelAdmin
from Proxy.models import MAC, Classi, Https
from Network.models import LAN, Management
from License.models import License
from License import bf
from prx_wcf import update_squid
import os
import gzip
from datetime import datetime
import subprocess


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


class ClassiAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ClassiAdmin, self).get_queryset(request)
        if request.user.is_staff and request.user.is_superuser:
            return qs
        return qs.filter(professori__professori=request.user)

    def get_actions(self, request):
        actions = super(ClassiAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def changelist_view(self, request, extra_context=None):
        if request.method == "POST":
            return super(ClassiAdmin, self).changelist_view(request)
        else:
            self.update_fw()
            return super(ClassiAdmin, self).changelist_view(request)

    def update_fw(self):
        manager = Management.objects.values()[0]['mac']
        mac_mgmnt = open(settings.FIREHOL_DIR + 'mac_allow', 'w')
        mac_mgmnt.write(manager+'\n')
        mac_mgmnt.close()
        file_mac_group_allow = open(settings.FIREHOL_DIR + 'mac_allow', 'a')
        internet_yes = MAC.objects.all().filter(classi=Classi.objects.all().filter(internet=True))
        for i in range(0, internet_yes.count()):
            file_mac_group_allow.write(str(internet_yes[i])+'\n')
        file_mac_group_allow.close()
        os.system("sudo firehol restart")

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            if obj.classi == 'LAN' or not str(request.user) == 'admin':
                messages.set_level(request, messages.ERROR)
                self.message_user(request,
                                  "Questo elemento non puo' essere rimosso, apartiene al sistema",
                                  level=messages.ERROR)
            else:
                data = ''.join(str(datetime.today())[:-7].split(':')).replace(' ', '-')
                tmp_sql = '/tmp/._.sql'
                os.system('mysqldump -u %s -h %s --password=%s %s --ignore-table=%s.aron_logs > %s'
                          % (settings.DATABASES.values()[0]['USER'], settings.DATABASES.values()[0]['HOST'],
                             settings.DATABASES.values()[0]['PASSWORD'], settings.DATABASES.values()[0]['NAME'],
                             settings.DATABASES.values()[0]['NAME'], tmp_sql))
                file_data = 'config.aron.prx-%s' % data
                file_save = gzip.open(settings.STATICFILES_DIRS[0] + '/' + file_data, 'wb')
                file_save.write(bf.crypt(open(tmp_sql, 'r').read()))
                file_save.close()
                os.unlink(tmp_sql)
                obj.delete()
                message_bit = "Elementi cancellato/i"
                self.message_user(request, "%s" % message_bit)

    really_delete_selected.short_description = 'Cancella elemento/i selezionato/i'

    list_display = ('link_classi', 'internet')
    list_editable = ('internet', )
    actions = [really_delete_selected]

    def __init__(self, *args, **kwargs):
        manager = Management.objects.values()[0]['mac']
        mac_mgmnt = open(settings.FIREHOL_DIR + 'mac_allow', 'w')
        mac_mgmnt.write(manager+'\n')
        mac_mgmnt.close()
        file_mac_group_allow = open(settings.FIREHOL_DIR + 'mac_allow', 'a')
        internet_yes = MAC.objects.all().filter(classi=Classi.objects.all().filter(internet=True))
        for i in range(0, internet_yes.count()):
            file_mac_group_allow.write(str(internet_yes[i])+'\n')
        file_mac_group_allow.close()
        os.system("sudo firehol restart")
        https = Https.objects.values()[0]['https']
        if https is True:
            update_squid(https=True)
        else:
            update_squid(https=False)
        super(ClassiAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )


class ProfessoriAdmin(admin.ModelAdmin):
    list_display = ('professori',)


class UpdateMACActionForm(ActionForm):
    loc = forms.ChoiceField(
            choices=((Classi.objects.values()[item]['classi'], Classi.objects.values()[item]['classi'])
                     for item in range(0, Classi.objects.all().count())))


class MACAdmin(admin.ModelAdmin):
    action_form = UpdateMACActionForm

    list_display = ('classi', 'name', 'mac', 'internet')
    list_filter = ('classi',)
    list_editable = ('internet',)

    def get_queryset(self, request):
        qs = super(MACAdmin, self).get_queryset(request)
        if request.user.is_staff and request.user.is_superuser:
            return qs
        return qs.filter(classi__professori__professori=request.user)

    def save_model(self, request, obj, form, change):
        if change is True:
            super(MACAdmin, self).save_model(request, obj, form, change)
        else:
            max_class = License.objects.values()[0]['qty_dev']
            devices = MAC.objects.all()
            if int(bf.decrypt(max_class)) is 0 \
                    or int(bf.decrypt(max_class)) > devices.count():
                super(MACAdmin, self).save_model(request, obj, form, change)
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "E' stato riaggiunto il numero massimo di dispositivi.")

    def move_mac_to_location(modeladmin, request, queryset):
        classi_id = Classi.objects.filter(classi=request.POST['loc']).values()[0]['id']
        for item in range(0, len(queryset)):
            mac = MAC.objects.get(mac=str(queryset[item]))
            mac.classi_id = classi_id
            mac.save()

    move_mac_to_location.short_description = 'Sposta MAC'

    def reload_classrooms(self):
        os.system("sudo /etc/init.d/apache2 reload")

    reload_classrooms.short_description = 'Ricarica locali'

    def update_fw(self):
        manager = Management.objects.values()[0]['mac']
        mac_mgmnt = open(settings.FIREHOL_DIR + 'mac_allow', 'w')
        mac_mgmnt.write(manager+'\n')
        mac_mgmnt.close()
        file_mac_group_allow = open(settings.FIREHOL_DIR + 'mac_allow', 'a')
        internet_yes = MAC.objects.all().filter(internet=True)
        for i in range(0, internet_yes.count()):
            file_mac_group_allow.write(str(internet_yes[i])+'\n')
        file_mac_group_allow.close()
        os.system("sudo firehol restart")

    update_fw.short_description = 'Applica cambiamenti'

    def get_actions(self, request):
        try:
            if request.POST['action'] == 'update_fw':
                self.update_fw()
                messages.set_level(request, messages.SUCCESS)
                actions = 'update_fw'
                return messages.success(request, "E' stato ricaricato il firewall.")
            elif request.POST['action'] == 'reload_classrooms':
                self.reload_classrooms()
                messages.set_level(request, messages.SUCCESS)
                actions = 'reload_classrooms'
                return messages.success(request, "E' stato ricaricati i dati.")
            else:
                actions = super(MACAdmin, self).get_actions(request)
                del actions['delete_selected']
                return actions
        except:
                actions = super(MACAdmin, self).get_actions(request)
                del actions['delete_selected']
                return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            if obj.classi == 'LAN' or not str(request.user) == 'admin':
                messages.set_level(request, messages.ERROR)
                self.message_user(request,
                                  "Questo elemento non puo' essere rimosso, apartiene al sistema",
                                  level=messages.ERROR)
            else:
                data = ''.join(str(datetime.today())[:-7].split(':')).replace(' ', '-')
                tmp_sql = '/tmp/._.sql'
                os.system('mysqldump -u %s -h %s --password=%s %s --ignore-table=%s.aron_logs > %s'
                          % (settings.DATABASES.values()[0]['USER'], settings.DATABASES.values()[0]['HOST'],
                             settings.DATABASES.values()[0]['PASSWORD'], settings.DATABASES.values()[0]['NAME'],
                             settings.DATABASES.values()[0]['NAME'], tmp_sql))
                file_data = 'config.aron.prx-%s' % data
                file_save = gzip.open(settings.STATICFILES_DIRS[0] + '/' + file_data, 'wb')
                file_save.write(bf.crypt(open(tmp_sql, 'r').read()))
                file_save.close()
                os.unlink(tmp_sql)
                obj.delete()
                message_bit = "Elemento/i cancellato/i"
                self.message_user(request, "%s" % message_bit)

    really_delete_selected.short_description = 'Cancella elemento/i selezionato/i'

    actions = [reload_classrooms, move_mac_to_location, really_delete_selected, update_fw]


class NewDevicesAdmin(admin.ModelAdmin):
    exclude = ('mac', 'data_import',)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        count = 0
        proc = subprocess.Popen("sudo egrep DHCPACK /var/log/syslog | grep -E 'to ([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2} \(' | awk '{print $10, $11}' | sort -n | uniq", shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            item = line.split()
            if MAC.objects.filter(mac=item[0]).exists():
                pass
            else:
                max_class = License.objects.values()[0]['qty_dev']
                devices = MAC.objects.all()
                if int(bf.decrypt(max_class)) is 0 or int(bf.decrypt(max_class)) > devices.count():
                    mac = MAC(mac=item[0], classi_id=1, internet=0, name=item[1][1:-1])
                    mac.save()
                    count += 1
                    if count is int(bf.decrypt(max_class)):
                        break
                    else:
                        continue
        proc.wait()
        if count > 0:
            messages.set_level(request, messages.INFO)
            msg = "Aggiunto/i %s dispositivo/i nuovi" % str(count)
            self.message_user(request, msg, level=messages.INFO)
        else:
            messages.set_level(request, messages.ERROR)
            self.message_user(request, "Non e' stato aggiunto nessun dispositivo nuovo", level=messages.ERROR)
        return super(NewDevicesAdmin, self).add_view(request, form_url, extra_context=extra_context)


class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('domain',)

    def get_actions(self, request):
        try:
            if request.POST['action'] == 'update_prx':
                self.update_prx()
                messages.set_level(request, messages.SUCCESS)
                actions = 'update_prx'
                return messages.success(request, "E' stato ricaricato il proxy.")
            else:
                actions = super(BlacklistAdmin, self).get_actions(request)
                del actions['delete_selected']
                return actions
        except:
                actions = super(BlacklistAdmin, self).get_actions(request)
                del actions['delete_selected']
                return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
            message_bit = "Elementi cancellato/i"
            self.message_user(request, "%s" % message_bit)

    really_delete_selected.short_description = 'Cancella elemento/i selezionato/i'

    def save_model(self, request, obj, form, change):
        super(BlacklistAdmin, self).save_model(request, obj, form, change)

    def update_prx(self):
        https = Https.objects.values()[0]['https']
        if https is True:
            update_squid(https=True)
        else:
            update_squid(https=False)

    update_prx.short_description = 'Applica cambiamenti'

    actions = [update_prx, really_delete_selected]


class HttpsAdmin(SingleModelAdmin):
    readonly_fields = ('disclaimer', 'certificato', 'manual')
    list_display = ('https',)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(HttpsAdmin, self).change_view(request, form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(HttpsAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        lan1 = LAN.objects.values()[0]['eth_ip_lan']
        check = form.cleaned_data['https']
        if check is True:
            fw_conf = 'SSL_WHITELIST="52.0.0.0/11\n' \
                      '               52.32.0.0/11\n' \
                      '               65.52.0.0/14\n' \
                      '               134.170.0.0/16\n' \
                      '               157.54.0.0/15\n' \
                      '               157.56.0.0/14\n' \
                      '               157.60.0.0/16\n' \
                      '               168.62.0.0/15\n' \
                      '               168.61.0.0/16\n' \
                      '               191.232.0.0/14"\n' \
                      'ipv4 transparent_proxy 443 3129 "root proxy" inface ' + lan1 + ' dst not "$SSL_WHITELIST"\n\n'
            f = open(settings.FIREHOL_DIR + '/firehol.conf', "r")
            contents = f.readlines()
            f.close()
            contents.insert(10, fw_conf)
            f = open(settings.FIREHOL_DIR + '/firehol.conf', "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
            update_squid(https=True)
        else:
            f = open(settings.FIREHOL_DIR + '/firehol.conf', "r")
            contents = f.readlines()
            f.close()
            del contents[10:21]
            f = open(settings.FIREHOL_DIR + '/firehol.conf', "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
            update_squid(https=False)
        super(HttpsAdmin, self).save_model(request, obj, form, change)
