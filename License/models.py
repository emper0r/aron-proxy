from __future__ import unicode_literals
from django.db import models
import datetime

class License(models.Model):
    year = datetime.timedelta(days=365)
    PROVINCE = (('AG', 'Agrigento'),
                ('AL', 'Alessandria'),
                ('AN', 'Ancona'),
                ('AO', 'Aosta'),
                ('AR', 'Arezzo'),
                ('AP', 'Ascoli Piceno'),
                ('AT', 'Asti'),
                ('AV', 'Avellino'),
                ('BA', 'Bari'),
                ('BT', 'Barletta-Andria-Trani'),
                ('BL', 'Belluno'),
                ('BN', 'Benevento'),
                ('BG', 'Bergamo'),
                ('BI', 'Biella'),
                ('BO', 'Bologna'),
                ('BZ', 'Bolzano'),
                ('BS', 'Brescia'),
                ('BR', 'Brindisi'),
                ('CA', 'Cagliari'),
                ('CL', 'Caltanissetta'),
                ('CB', 'Campobasso'),
                ('CI', 'Carbonia-Iglesias'),
                ('CE', 'Caserta'),
                ('CT', 'Catania'),
                ('CZ', 'Catanzaro'),
                ('CH', 'Chieti'),
                ('CO', 'Como'),
                ('CS', 'Cosenza'),
                ('CR', 'Cremona'),
                ('KR', 'Crotone'),
                ('CN', 'Cuneo'),
                ('EN', 'Enna'),
                ('FM', 'Fermo'),
                ('FE', 'Ferrara'),
                ('FI', 'Firenze'),
                ('FG', 'Foggia'),
                ('FC', 'Forli-Cesena'),
                ('FR', 'Frosinone'),
                ('GE', 'Genova'),
                ('GO', 'Gorizia'),
                ('GR', 'Grosseto'),
                ('IM', 'Imperia'),
                ('IS', 'Isernia'),
                ('32', 'La'),
                ('AQ', 'L\'Aquila'),
                ('LT', 'Latina'),
                ('LE', 'Lecce'),
                ('LC', 'Lecco'),
                ('LI', 'Livorno'),
                ('LO', 'Lodi'),
                ('LU', 'Lucca'),
                ('MC', 'Macerata'),
                ('MN', 'Mantova'),
                ('MS', 'Massa-Carrara'),
                ('MT', 'Matera'),
                ('VS', 'Medio Campidano'),
                ('ME', 'Messina'),
                ('MI', 'Milano'),
                ('MO', 'Modena'),
                ('MB', 'Monza e della Brianza'),
                ('NA', 'Napoli'),
                ('NO', 'Novara'),
                ('NU', 'Nuoro'),
                ('OT', 'Olbia-Tempio'),
                ('OR', 'Oristano'),
                ('PD', 'Padova'),
                ('PA', 'Palermo'),
                ('PR', 'Parma'),
                ('PV', 'Pavia'),
                ('PG', 'Perugia'),
                ('PU', 'Pesaro e Urbino'),
                ('PE', 'Pescara'),
                ('PC', 'Piacenza'),
                ('PI', 'Pisa'),
                ('PT', 'Pistoia'),
                ('PN', 'Pordenone'),
                ('PZ', 'Potenza'),
                ('PO', 'Prato'),
                ('RG', 'Ragusa'),
                ('RA', 'Ravenna'),
                ('97', 'Reggio Calabria'),
                ('45', 'Reggio Emilia'),
                ('RI', 'Rieti'),
                ('RN', 'Rimini'),
                ('RM', 'Roma'),
                ('RO', 'Rovigo'),
                ('SA', 'Salerno'),
                ('SS', 'Sassari'),
                ('SV', 'Savona'),
                ('SI', 'Siena'),
                ('SR', 'Siracusa'),
                ('SO', 'Sondrio'),
                ('TA', 'Taranto'),
                ('TE', 'Teramo'),
                ('TR', 'Terni'),
                ('TO', 'Torino'),
                ('OG', 'Ogliastra'),
                ('TP', 'Trapani'),
                ('TN', 'Trento'),
                ('TV', 'Treviso'),
                ('TS', 'Trieste'),
                ('UD', 'Udine'),
                ('VA', 'Varese'),
                ('VE', 'Venezia'),
                ('VB', 'Verbano-Cusio-Ossola'),
                ('VC', 'Vercelli'),
                ('VR', 'Verona'),
                ('VV', 'Vibo Valentina'),
                ('VI', 'Vicenza'),
                ('VT', 'Viterbo'))
    client = models.CharField('Nome cliente', max_length=64, help_text="Nominativo cliente")
    province = models.CharField('Provincia', max_length=16, choices=PROVINCE, help_text="Seleziona la provincia")
    req = models.CharField('Richiesta', max_length=64, help_text="Inserice il codice licenza")
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
