from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from Internet.models import Classi
from Internet.models import IP
from Internet.models import MAC
from Internet.models import WebContentFilter
from Internet.models import Professori


class ClassiAdmin(admin.ModelAdmin):
    list_display = ('group', 'internet')
    list_filter = ('internet',)


class ProfessoriAdmin(admin.ModelAdmin):
    list_display = ('professori',)


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


admin.site.register(Classi, ClassiAdmin)
admin.site.register(IP, IPAdmin)
admin.site.register(MAC, MACAdmin)
admin.site.register(WebContentFilter, WebContentFilterAdmin)
admin.site.register(Professori, ProfessoriAdmin)
