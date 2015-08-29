from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
from django.contrib import admin, messages
from singlemodeladmin import SingleModelAdmin
from Internet.models import NewDevices


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

    list_display = ('link_classi', 'internet')
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

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(WebContentFilterAdmin, self).add_view(request, form_url, extra_context=extra_context)


class NewDevicesAdmin(admin.ModelAdmin):
    readonly_fields = ('new_devices',)
    exclude = ('mac', 'ip')

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_as_new'] = False
        extra_context['show_delete_link'] = False
        return super(NewDevicesAdmin, self).add_view(request, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        aux = NewDevices.objects.all()
        aux.delete()
        if aux.count() is 0:
            messages.set_level(request, messages.ERROR)
            self.message_user(request, "Non e' stato riaggiunto nessun dispositivo nuovo", level=messages.ERROR)
            return
        else:
            super(NewDevicesAdmin, self).save_model(request, obj, form, change)
