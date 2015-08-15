from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django import forms
import re

MAC_RE = r'^([0-9a-fA-F]{2}([:]|$)){6}$'
mac_re = re.compile(MAC_RE)

class MACAddressFormField(forms.fields.RegexField):
    default_error_messages = {
        'invalid': _(u'Enter a valid MAC address.'),
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

class IP(models.Model):
    netmasks = (
        ('255.255.255.252', '255.255.255.252'),
        ('255.255.255.248', '255.255.255.248'),
        ('255.255.255.240', '255.255.255.240'),
        ('255.255.255.0', '255.255.255.0'),
        ('255.255.0.0', '255.255.0.0'),
        ('255.0.0.0', '255.0.0.0'),
    )
    ip_wan = models.GenericIPAddressField('WAN',
                                          unique=True,
                                          max_length=15,
                                          blank=False,
                                          null=False,
                                          help_text='Indirizzo IP lato Internet')
    mask_wan = models.CharField('Netmask',
                                max_length=17,
                                choices=netmasks,
                                null=False,
                                unique=True,
                                help_text='Seleziona maschera rete WAN')
    gateway = models.GenericIPAddressField('Gateway',
                                           unique=True,
                                           max_length=15,
                                           blank=False,
                                           null=False,
                                           help_text='Porta Gateway di uscita a Internet')
    dns1 = models.GenericIPAddressField('DNS 1:',
                                        unique=True,
                                        max_length=15,
                                        blank=False,
                                        null=False,
                                        help_text='DNS primario')
    dns2 = models.GenericIPAddressField('DNS 2:',
                                        unique=True,
                                        max_length=15,
                                        blank=False,
                                        help_text='DNS secondario')
    ip_lan = models.GenericIPAddressField('LAN',
                                      unique=True,
                                      max_length=15,
                                      blank=False,
                                      null=False,
                                      help_text='Indirizzo IP della rete Interna')
    mask_lan = models.CharField('Netmask',
                                max_length=17,
                                choices=netmasks,
                                null=False,
                                unique=True,
                                help_text='Seleziona maschera rete lato LAN')

    dhcp = models.BooleanField('DHCP abilitato', default=True)
    ip_start = models.GenericIPAddressField('Indirizzo IP inizio', max_length=15)
    ip_end = models.GenericIPAddressField('Indirizzo IP finale', max_length=15)

    def __unicode__(self):
        return 'Network'

    class Meta:
        verbose_name_plural = "Impostazioni"


class MAC(models.Model):
    mac = MACAddressField('Indirizzo MAC',
                          blank=False,
                          unique=True,
                          help_text='Obbligatorio. Devi inserire la MAC in formato AA:BB:CC:DD:EE:FF')

    def __unicode__(self):
        return self.mac

    class Meta:
        verbose_name = "MAC"

    def save(self, *args, **kwargs):
        super(MAC, self).save(*args, **kwargs)
