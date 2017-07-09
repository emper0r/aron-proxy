from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django import forms
from Proxy.models import MAC
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


class Choices(models.Model):
    type = models.CharField(max_length=1)


class WAN(models.Model):
    netmasks = (
        ('255.255.255.252', '255.255.255.252'),
        ('255.255.255.248', '255.255.255.248'),
        ('255.255.255.240', '255.255.255.240'),
        ('255.255.255.224', '255.255.255.224'),
        ('255.255.255.192', '255.255.255.192'),
        ('255.255.255.128', '255.255.255.128'),
        ('255.255.255.0', '255.255.255.0'),
        ('255.255.252.0', '255.255.252.0'),
        ('255.255.0.0', '255.255.0.0'),
        ('255.0.0.0', '255.0.0.0'),
    )
    eth_ip_wan = models.CharField('Device WAN', unique=True, max_length=16, blank=False, null=False)
    ip_wan = models.GenericIPAddressField('WAN', unique=True, max_length=15, blank=False, null=False, help_text='Indirizzo IP lato Internet')
    mask_wan = models.CharField('Netmask', max_length=17, choices=netmasks, null=False, unique=True, help_text='Seleziona maschera rete WAN')
    gateway = models.GenericIPAddressField('Gateway', unique=True, max_length=15, blank=False, null=False, help_text='Porta Gateway ad Internet')
    dns1 = models.GenericIPAddressField('DNS 1:', unique=True, max_length=15, blank=False, null=False, help_text='DNS primario obbligatorio: Ad esempio 8.8.8.8')
    dns2 = models.GenericIPAddressField('DNS 2:', unique=True, max_length=15, blank=False, help_text='DNS secondario obbligatorio: Ad esempio 8.8.4.4')

    def __unicode__(self):
        return 'Impostazione WAN'

    class Meta:
        verbose_name_plural = "Impostazione WAN"


class LAN(models.Model):
    netmasks = (
        ('255.255.255.252', '255.255.255.252'),
        ('255.255.255.248', '255.255.255.248'),
        ('255.255.255.240', '255.255.255.240'),
        ('255.255.255.224', '255.255.255.224'),
        ('255.255.255.192', '255.255.255.192'),
        ('255.255.255.128', '255.255.255.128'),
        ('255.255.255.0', '255.255.255.0'),
        ('255.255.252.0', '255.255.252.0'),
        ('255.255.0.0', '255.255.0.0'),
        ('255.0.0.0', '255.0.0.0'),
    )
    eth_ip_lan = models.CharField('Device LAN', unique=True, max_length=16, blank=False, null=False, help_text='Selezionare un\'interfaccia per associare')
    ip_lan = models.GenericIPAddressField('LAN', unique=True, max_length=15, blank=False, null=False, help_text='Indirizzo IP della rete LAN')
    mask_lan = models.CharField('Netmask', max_length=17, choices=netmasks, null=False, unique=False, help_text='Seleziona maschera rete LAN')
    dhcp = models.BooleanField('DHCP abilitato', default=True)
    ip_start = models.GenericIPAddressField('Indirizzo IP inizio', max_length=15)
    ip_end = models.GenericIPAddressField('Indirizzo IP finale', max_length=15)

    def __unicode__(self):
        return 'Impostazione LAN'

    class Meta:
        verbose_name_plural = "Impostazione LAN"


class dhcptable(models.Model):
    name = models.CharField('Nome device', max_length='20', blank=False, unique=True, help_text='Nome identificativo per il device')
    mac = MACAddressField('MAC Address', blank=False, unique=True, help_text="Obbligatorio. Devi inserire la MAC in formato AA:BB:CC:DD:EE:FF")
    ip = models.IPAddressField('Indirizzo IP', max_length='15', unique=True, blank=False, help_text="Indirizzo IPv4 per la rete impostata nel DHCP server")

    def __unicode__(self):
        return 'Impostazioni DHCP per IP fisso'

    class Meta:
        verbose_name_plural = "Impostazioni DHCP"


class Management(models.Model):
    mac = MACAddressField('Indirizzo MAC - PC Admin', blank=False, unique=True, help_text='Obbligatorio. Devi inserire la MAC in formato AA:BB:CC:DD:EE:FF')

    def __unicode__(self):
        return self.mac

    class Meta:
        verbose_name_plural = "MAC Management"

    def save(self, *args, **kwargs):
        super(Management, self).save(*args, **kwargs)


class Apply(models.Model):
    data_import = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.data_import)

    class Meta:
        verbose_name_plural = "Applica Cambiamenti"

