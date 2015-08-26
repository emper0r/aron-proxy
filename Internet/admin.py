from django.contrib import admin, messages
from singlemodeladmin import SingleModelAdmin
from Internet.models import NewDevices

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

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            if obj.classi == 'autodiscover':
                messages.set_level(request, messages.ERROR)
                self.message_user(request,
                                  "Questo elemento non puo' essere rimosso, apartiene al interno del sistema",
                                  level=messages.ERROR)
            else:
                obj.delete()
                message_bit = "Elementi cancellato/i"
                self.message_user(request, "%s" % message_bit)

    really_delete_selected.short_description = 'Cancella elemento/i selezionato/i'

    list_display = ('classi', 'internet')
    list_filter = ('internet',)
    actions = [really_delete_selected]

    def __init__(self, *args, **kwargs):
        super(ClassiAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

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
    readonly_fields = ('new_devices',)
    exclude = ('data_import',)

    def save_model(self, request, obj, form, change):
        aux = NewDevices.objects.all()
        aux.delete()
        super(NewDevicesAdmin, self).save_model(request, obj, form, change)
