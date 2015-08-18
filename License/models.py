from __future__ import unicode_literals
from django.db import models
import datetime

class License(models.Model):
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
    lic_a = models.CharField('Licenza A', max_length=64, help_text="Inserice il codice licenza")
    lic_b = models.CharField('Licenza B', max_length=64, help_text="Inserice il codice licenza")
    exp_lic = models.DateField('Scandenza licenza', default=datetime.date.today)

    def __str__(self):
        return self.client

    def masq_A(self):
        lic_items = License.objects.all()
        lic_a = lic_items.values()[0]['lic_a']
        return str(lic_a).replace(lic_a, '*' * len(lic_a))

    masq_A.short_description = 'Licenza A'

    def masq_B(self):
        lic_items = License.objects.all()
        lic_b = lic_items.values()[0]['lic_b']
        return str(lic_b).replace(lic_b, '*' * len(lic_b))

    masq_B.short_description = 'Licenza B'

    lic_masq_a = property(masq_A)
    lic_masq_b = property(masq_B)
