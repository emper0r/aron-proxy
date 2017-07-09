from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django import forms
from License.models import License
import re


MAC_RE = r'^([0-9a-fA-F]{2}([:]|$)){6}$'
mac_re = re.compile(MAC_RE)


class MACAddressFormField(forms.fields.RegexField):
    default_error_messages = {
        'invalid': _(u'Inserice un indirizzo MAC valido.'),
    }

    def __init__(self, *args, **kwargs):
        super(MACAddressFormField, self).__init__(mac_re, *args, **kwargs)


class MACAddressField(models.Field):
    empty_strings_allowed = False

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 17
        super(MACAddressField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        defaults = {'form_class': MACAddressFormField}
        defaults.update(kwargs)
        return super(MACAddressField, self).formfield(**defaults)


class Classi(models.Model):
    classi = models.CharField('Nome di Locale',
                              max_length='20',
                              unique=True,
                              help_text='Obbligatorio. (Esempio: Aula, Classe, Ufficio)')
    internet = models.BooleanField(default=None)

    def __unicode__(self):
        return self.classi

    class Meta:
        verbose_name_plural = "Gestione - Locale"

    def link_classi(self):
        room = Classi.objects.all()
        for c in range(0, room.count()):
            if self.classi == 'LAN':
                return u"%s" % self.classi
            else:
                return u"<a href='%d/'>%s</a>" % (self.id, self.classi)

    link_classi.short_description = ''
    link_classi.allow_tags = True

    def save(self, *args, **kwargs):
        MAC.objects.filter(classi_id=self.id).update(internet=self.internet)
        super(Classi, self).save(*args, **kwargs)


class Professori(models.Model):
    professori = models.ForeignKey(User)
    classi = models.ManyToManyField(Classi)

    def __unicode__(self):
        return unicode(self.professori)

    class Meta:
        verbose_name_plural = "Associazione Classi a Docente"


class MAC(models.Model):
    classi = models.ForeignKey(Classi)
    name = models.CharField('nome_dispositivo', max_length=64, default='senza_nome', null=True, blank=True)
    mac = MACAddressField('Indirizzo MAC',
                          blank=False,
                          unique=True,
                          help_text='Obbligatorio. Devi inserire la MAC in formato AA:BB:CC:DD:EE:FF')
    internet = models.BooleanField(default=None)

    def __unicode__(self):
        return self.mac

    class Meta:
        verbose_name_plural = "Gestione - MAC"

    def save(self, *args, **kwargs):
        super(MAC, self).save(*args, **kwargs)


class NewDevices(models.Model):
    data_import = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.data_import)

    class Meta:
        verbose_name_plural = "Dispositivi nuovi"


class Blacklist(models.Model):
    domain = models.CharField("Sitio / Dominio:",
                              max_length=255, unique=True, blank=True,
                              help_text="Esempio: facebook.com o www.google.it")

    def __unicode__(self):
        return self.domain

    class Meta:
        verbose_name_plural = "Lista nera"


class Https(models.Model):
    https = models.BooleanField("Attivazione HTTPS inspection (BETA)", default=False,
                                help_text="La attivazione di questa opzione viene eseguita con disclaimer da parte Computer Time s.r.l")

    class Meta:
        verbose_name_plural = "HTTPS Inspection (BETA)"

    def disclaimer(self):
        message = "<strong>*** ATTENZIONE ***</strong><br>- Il Protocollo HTTPS e' stato progettato per offrire agli utenti una aspettativa di privacy e sicurezza.<br>" \
                  "- Decifrare HTTPS tunnel senza il consenso dell'utente  viola le norme etiche e puo\' essere illegale nella propria giurisdizione.<br>" \
                  "- Le caratteristiche di decrittazione descritte qui e altrove sono progettate per la distribuzione con il consenso dell\'utente o almeno in ambienti in cui la decrittazione senza il consenso e' legale.<br>" \
                  "- Queste caratteristiche illustrano il motivo per cui gli utenti che utilizzano il proxy in questa modalita\' devono stare attenti alla loro navigazione in quanto <strong>NON PIU\' SICURA</strong>.<br>" \
                  "- Decifrare HTTPS tunnel costituisce un attacco man-in-the-middle dal punto di sicurezza di rete.<br>- Strumenti di questo genere sono l\'equivalente di una bomba atomica nel mondo reale.<br> <strong>***** Assicurarsi di aver compreso quello che state facendo *****</strong> <br>assumendoVi le Vostre responsabilita\' decisionali." \
                  "Alla luce di quato sopra descritto fate scelte sagge!."
        return message

    disclaimer.short_description = "Disclaimer"
    disclaimer.allow_tags = True

    def certificato(self):
        return "<a href=\"../../../static/aron-proxy.der\">aron-proxy.der</a>"

    certificato.allow_tags = True
    certificato.description = 'Scarica'

    def manual(self):
        return "<a href=\"../../../static/Certificato_Aron_Proxy.pdf\">Come Importare il Certificato</a>"

    manual.allow_tags = True
    manual.description = 'Manuale per Importare il Certificato sul Browser'
