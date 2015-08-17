from django.contrib import admin, messages
from Posta.models import VeximDomains, VeximUsers
from License.models import License

class VeximDomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'enabled', 'avscan', 'spamassassin', 'max_accounts')
    list_filter = ('enabled',)
    exclude = ('uid', 'gid', 'pipe', 'maildir', 'blocklists', 'complexpass')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['max_accounts']
        else:
            return []


class VeximUserAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'domain',
                    'on_avscan',
                    'on_spamassassin',
                    'on_vacation',
                    'quota',
                    'enabled')
    list_filter = ('enabled',)
    ordering = ('user',)
    exclude = ('username',
               'passwd',
               'uid',
               'gid',
               'smtp',
               'pop',
               'on_piped',
               'type',
               'localpart',
               'on_blocklist',
               'on_complexpass')

    def save_model(self, request, obj, form, change):
        max_accounts = VeximDomains.objects.all()
        accounts = VeximUsers.objects.all()
        if int(max_accounts.values()[0]['max_accounts']) is 0 \
                or int(max_accounts.values()[0]['max_accounts']) > accounts.count():
            super(VeximUserAdmin, self).save_model(request, obj, form, change)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "E' stato riaggiunto il massimo accounts.")

k = License.objects.all().count()
if k > 0:
    admin.site.register(VeximDomains, VeximDomainAdmin)
    admin.site.register(VeximUsers, VeximUserAdmin)
