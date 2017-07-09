from __future__ import unicode_literals
from django.db import models
import datetime
import bf


class License(models.Model):
    year = datetime.timedelta(days=365)
    client = models.CharField('Nome cliente', max_length=64)
    name = models.CharField('Nominativo', max_length=64)
    province = models.CharField('Provincia', max_length=16)
    qty_dev = models.CharField('Numero di Dispositivi Massimi', max_length=255, unique=True, blank=False)
    req = models.CharField('Codice', max_length=255, help_text="Inserice il codice inviato nella mail")
    lic = models.CharField('Licenza', max_length=255, help_text="Inserice la licenza inviata nella mail")
    exp_lic = models.CharField('Scandenza licenza', max_length=64)

    def __str__(self):
        return self.client

    def masq_req(self):
        lic_items = License.objects.all()
        req = lic_items.values()[0]['req']
        return str(req).replace(req, '*' * len(req))

    masq_req.short_description = 'Codice'

    def masq_lic(self):
        lic_items = License.objects.all()
        lic = lic_items.values()[0]['lic']
        return str(lic).replace(lic, '*' * len(lic))

    masq_lic.short_description = 'Licenza'

    def masq_date(self):
        items = License.objects.all()
        date = bf.decrypt(items.values()[0]['exp_lic'])
        return date

    masq_date.short_description = 'Scadenza Licenza'

    def masq_qty_dev(self):
        items = License.objects.all()
        qty_dev = bf.decrypt(items.values()[0]['qty_dev'])
        if qty_dev is str(0):
            qty_dev = 'Illimitato'
        return qty_dev

    masq_qty_dev.short_description = 'Numero di Dispositivi Massimi Gestibili'

    lic_masq_req = property(masq_req)
    lic_masq_lic = property(masq_lic)
    date_masq_date = property(masq_date)
    masq_qty_class = property(masq_qty_dev)
