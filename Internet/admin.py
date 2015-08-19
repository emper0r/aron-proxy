from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

class ClassiAdmin(admin.ModelAdmin):
    list_display = ('classi', 'internet')
    list_filter = ('internet',)

    def get_queryset(self, request):
        qs = super(ClassiAdmin, self).get_queryset(request)
        if request.user.is_staff and request.user.is_superuser:
            return qs
        return qs.filter(professori__professori=request.user)

class ProfessoriAdmin(admin.ModelAdmin):
    list_display = ('professori',)


class IPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'classi',)
    list_filter = ('classi',)


class MACAdmin(admin.ModelAdmin):
    list_display = ('mac', 'classi',)
    list_filter = ('classi',)


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


class NewDevicesAdmin(admin.ModelAdmin):
    pass
