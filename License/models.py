from __future__ import unicode_literals
from django.db import models
import datetime

class License(models.Model):
    year = datetime.timedelta(days=365)
    client = models.CharField('Nome cliente', max_length=64)
    province = models.CharField('Provincia', max_length=16)
    req = models.CharField('Richiesta', max_length=64, help_text="Inserice il codice richiesta")
    lic = models.CharField('Licenza', max_length=64, help_text="Inserice il codice licenza")
    exp_date = datetime.datetime.today() + (year * 3)
    exp_lic = models.DateField('Scandenza licenza', default=exp_date)

    def __str__(self):
        return self.client

    def masq_req(self):
        lic_items = License.objects.all()
        req = lic_items.values()[0]['req']
        return str(req).replace(req, '*' * len(req))

    masq_req.short_description = 'Richiesta'

    def masq_lic(self):
        lic_items = License.objects.all()
        lic = lic_items.values()[0]['lic']
        return str(lic).replace(lic, '*' * len(lic))

    masq_lic.short_description = 'Licenza'

    lic_masq_a = property(masq_req)
    lic_masq_b = property(masq_lic)
