from django.contrib import admin
from django.contrib import messages
from singlemodeladmin import SingleModelAdmin
from aron.models import Classi
from aron.models import IP
from aron.models import MAC
from aron.models import WebContentFilter
from aron.models import Professori
from aron.models import VeximDomains
from aron.models import VeximUsers


class ClassiAdmin(admin.ModelAdmin):
    list_display = ('group', 'internet')
    list_filter = ('internet',)

class ProfessoriAdmin(admin.ModelAdmin):
    # list_display = ('professori',)
    pass


class IPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'groups',)
    list_filter = ('groups',)


class MACAdmin(admin.ModelAdmin):
    list_display = ('mac', 'groups',)
    list_filter = ('groups',)


class WebContentFilterAdmin(SingleModelAdmin):
    list_display = ('abortion', 'ads', 'adult', 'aggressive', 'antispyware',
                    'artnudes', 'astrology', 'banking', 'beerliquorinfo', 'beerliquorsale',
                    'blog', 'cellphones', 'chat', 'childcare', 'cleaning',
                    'clothing', 'contraception', 'culnary', 'dating', 'desktopsillies',
                    'dialers', 'drugs', 'ecommerce', 'entertainment', 'filehosting',
                    'frencheducation', 'gambling', 'games', 'gardening', 'government',
                    'guns', 'hacking', 'homerepair', 'hygiene', 'instantmessaging',
                    'jewelry', 'jobsearch', 'kidstimewasting', 'mail', 'marketingware',
                    'medical', 'mixed_adult', 'naturism', 'news', 'onlineauctions',
                    'onlinegames', 'onlinepayment', 'personalfinance', 'pets', 'phishing',
                    'porn', 'proxy', 'radio', 'religion', 'ringtones',
                    'searchengines', 'sect', 'sexuality', 'sexualityeducation',
                    'shopping', 'socialnetworking', 'sportnews', 'sports', 'spyware',
                    'updatesites', 'vacation', 'violence', 'virusinfected', 'warez',
                    'weather', 'weapons', 'webmail', 'whitelist')


class VeximDomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'enabled', 'avscan', 'spamassassin', 'max_accounts')
    list_filter = ('enabled',)
    exclude = ('uid', 'gid', 'pipe', 'maildir', 'blocklists', 'complexpass')
    # readonly_fields = ('max_accounts',)

    def get_readonly_fields(self, request, obj=None):
        if obj is None or obj is not request.user.is_superuser:
            return self.readonly_fields
        else:
            return self.model._meta.get_all_field_names()


class VeximUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'domain', 'on_avscan', 'on_spamassassin', 'on_vacation', 'quota', 'enabled')
    list_filter = ('enabled',)
    ordering = ('user',)
    exclude = ('username', 'passwd', 'uid', 'gid', 'smtp', 'pop', 'on_piped', 'type', 'localpart', 'on_blocklist', 'on_complexpass')

    def save_model(self, request, obj, form, change):
        max_accounts = VeximDomains.objects.all()
        accounts = VeximUsers.objects.all()
        if int(max_accounts.values()[0]['max_accounts']) is 0 or int(max_accounts.values()[0]['max_accounts']) > accounts.count():
            super(VeximUserAdmin, self).save_model(request, obj, form, change)
        else:
            messages.error(request, "E' stato riaggiunto il massimo accounts.")


admin.site.register(Classi, ClassiAdmin)
admin.site.register(IP, IPAdmin)
admin.site.register(MAC, MACAdmin)
admin.site.register(WebContentFilter, WebContentFilterAdmin)
# admin.site.register(Professori, ProfessoriAdmin)
admin.site.register(VeximDomains, VeximDomainAdmin)
admin.site.register(VeximUsers, VeximUserAdmin)
