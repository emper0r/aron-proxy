from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from aron.models import Classes
from aron.models import IP
from aron.models import MAC
from aron.models import WebContentFilter
from aron.models import VeximDomains
from aron.models import VeximUsers

class ClassesAdmin(admin.ModelAdmin):
    list_display = ('group', 'internet')
    list_filter = ('internet',)

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
    readonly_fields = ('max_accounts',)

class VeximUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'domain', 'on_avscan', 'on_spamassassin', 'on_vacation', 'quota', 'enabled')
    list_filter = ('enabled',)
    ordering = ('user',)
    exclude = ('username', 'passwd', 'uid', 'gid', 'smtp', 'pop', 'on_piped', 'type', 'localpart', 'on_blocklist', 'on_complexpass')

    # def clean(self):
    #     max_accounts = VeximDomains.objects.all()
    #     accounts = VeximUsers.objects.all()
    #     if int(max_accounts.values()[0]['max_accounts']) < accounts.count():
    #         raise ValidationError('E\' stato riaggiunto il numero massimo di accounts')

admin.site.register(Classes, ClassesAdmin)
admin.site.register(IP, IPAdmin)
admin.site.register(MAC, MACAdmin)
admin.site.register(WebContentFilter, WebContentFilterAdmin)
admin.site.register(VeximDomains, VeximDomainAdmin)
admin.site.register(VeximUsers, VeximUserAdmin)
