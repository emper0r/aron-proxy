from django.contrib import admin
from django.contrib import messages
from singlemodeladmin import SingleModelAdmin
from License.models import License
import key

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
                messages.set_level(request, messages.INFO)
                messages.error(request, "Licenza valida, attivazione eseguita con esito!")

            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Licenza invalida, chiede assistenza a Computer Time s.r.l")
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Licenza e gia' attivata.")


admin.site.register(License, LicAdmin)
