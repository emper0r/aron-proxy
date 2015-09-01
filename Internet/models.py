from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django import forms
import subprocess
import re
import os

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
    classi = models.CharField('Nome della Classe',
                             max_length='20',
                             unique=True,
                             help_text='Obbligatorio. Identificativo della Classe')
    internet = models.BooleanField(default=False)

    def __unicode__(self):
        return self.classi

    class Meta:
        verbose_name_plural = "Gestione - Classi"

    def link_classi(self):
        room = Classi.objects.all()
        for c in range(0, room.count()):
            if self.classi == 'autodiscover':
                return u"%s" % self.classi
            else:
                return u"<a href='%d/'>%s</a>" % (self.id, self.classi)

    link_classi.short_description = ''
    link_classi.allow_tags = True

    def save(self, *args, **kwargs):
        super(Classi, self).save(*args, **kwargs)
        update_squid()


class Professori(models.Model):
    professori = models.ForeignKey(User)
    classi = models.ManyToManyField(Classi)

    def __unicode__(self):
        return unicode(self.professori)

    class Meta:
        verbose_name_plural = "Associazione Classi a Docente"


class IP(models.Model):
    classi = models.ForeignKey(Classi)
    ip = models.GenericIPAddressField('Indirizzo IP',
                                      unique=True,
                                      max_length=15,
                                      blank=False,
                                      null=False,
                                      help_text='Indirizzo IP')

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name_plural = "Gestione - IP"

    def save(self, *args, **kwargs):
        super(IP, self).save(*args, **kwargs)
        update_squid()


class MAC(models.Model):
    classi = models.ForeignKey(Classi)
    mac = MACAddressField('Indirizzo MAC',
                          blank=False,
                          unique=True,
                          help_text='Obbligatorio. Devi inserire la MAC in formato AA:BB:CC:DD:EE:FF')

    def __unicode__(self):
        return self.mac

    class Meta:
        verbose_name_plural = "Gestione - MAC"

    def save(self, *args, **kwargs):
        super(MAC, self).save(*args, **kwargs)
        update_squid()


class WebContentFilter(models.Model):
    abortion = models.BooleanField(default=False, help_text='Abortion information excluding when related to religion')
    ads = models.BooleanField(default=False, help_text='Advert servers and banned URLs')
    adult = models.BooleanField(default=False, help_text='Sites containing adult material such as swearing but not porn')
    aggressive = models.BooleanField(default=False, help_text='Similar to violence but more promoting than depicting')
    antispyware = models.BooleanField(default=False, help_text='Sites that remove spyware')
    artnudes = models.BooleanField(default=False, help_text='Art sites containing artistic nudity')
    astrology = models.BooleanField(default=False, help_text='Astrology websites')
    banking = models.BooleanField(default=False, help_text='Banking websites')
    beerliquorinfo = models.BooleanField(default=False, help_text='Sites with information only on beer or liquors')
    beerliquorsale = models.BooleanField(default=False, help_text='Sites with beer or liquors for sale')
    blog = models.BooleanField(default=False, help_text='Journal/Diary websites')
    cellphones = models.BooleanField(default=False, help_text='Stuff for mobile/cell phones')
    chat = models.BooleanField(default=False, help_text='Sites with chat rooms etc')
    childcare = models.BooleanField(default=False, help_text='Sites to do with childcare')
    cleaning = models.BooleanField(default=False, help_text='Sites to do with cleaning')
    clothing = models.BooleanField(default=False, help_text='Sites about and selling clothing')
    contraception = models.BooleanField(default=False, help_text='Information about contraception')
    culnary = models.BooleanField(default=False, help_text='Sites about cooking et al')
    dating = models.BooleanField(default=False, help_text='Sites about dating')
    desktopsillies = models.BooleanField(default=False, help_text='Sites containing screen savers, backgrounds, cursers, pointers. desktop themes and similar timewasting and potentially dangerous content')
    dialers = models.BooleanField(default=False, help_text='Sites with dialers such as those for pornography or trojans')
    drugs = models.BooleanField(default=False, help_text='Drug related sites')
    ecommerce = models.BooleanField(default=False, help_text='Sites that provide online shopping')
    entertainment = models.BooleanField(default=False, help_text='Sites that promote movies, books, magazine, humor')
    filehosting = models.BooleanField(default=False, help_text='Sites to do with filehosting')
    frencheducation = models.BooleanField(default=False, help_text='Sites to do with french education')
    gambling = models.BooleanField(default=False, help_text='Gambling sites including stocks and shares')
    games = models.BooleanField(default=False, help_text='Game related sites')
    gardening = models.BooleanField(default=False, help_text='Gardening sites')
    government = models.BooleanField(default=False, help_text='Military and schools etc')
    guns = models.BooleanField(default=False, help_text='Sites with guns')
    hacking = models.BooleanField(default=False, help_text='Hacking/cracking information')
    homerepair = models.BooleanField(default=False, help_text='Sites about home repair')
    hygiene = models.BooleanField(default=False, help_text='Sites about hygiene and other personal grooming related stuff')
    instantmessaging = models.BooleanField(default=False, help_text='Sites that contain messenger client download and web-based messaging sites')
    jewelry = models.BooleanField(default=False, help_text='Sites about and selling jewelry')
    jobsearch = models.BooleanField(default=False, help_text='Sites for finding jobs')
    kidstimewasting = models.BooleanField(default=False, help_text='Sites kids often waste time on')
    mail = models.BooleanField(default=False, help_text='Webmail and email sites')
    marketingware = models.BooleanField(default=False, help_text='Sites about marketing products')
    medical = models.BooleanField(default=False, help_text='Medical websites')
    mixed_adult = models.BooleanField(default=False, help_text='Mixed adult content sites')
    naturism = models.BooleanField(default=False, help_text='Sites that contain nude pictures and/or promote a nude lifestyle')
    news = models.BooleanField(default=False, help_text='News sites')
    onlineauctions = models.BooleanField(default=False, help_text='Online auctions')
    onlinegames = models.BooleanField(default=False, help_text='Online gaming sites')
    onlinepayment = models.BooleanField(default=False, help_text='Online payment sites')
    personalfinance = models.BooleanField(default=False, help_text='Personal finance sites')
    pets = models.BooleanField(default=False, help_text='Pet sites')
    phishing = models.BooleanField(default=False, help_text='Sites attempting to trick people into giving out private information.')
    porn = models.BooleanField(default=False, help_text='Pornography')
    proxy = models.BooleanField(default=False, help_text='Sites with proxies to bypass filters')
    radio = models.BooleanField(default=False, help_text='non-news related radio and television')
    religion = models.BooleanField(default=False, help_text='Sites promoting religion')
    ringtones = models.BooleanField(default=False, help_text='Sites containing ring tones, games, pictures and other')
    searchengines = models.BooleanField(default=False, help_text='Search engines such as google')
    sect = models.BooleanField(default=False, help_text='Sites about eligious groups')
    sexuality = models.BooleanField(default=False, help_text='Sites dedicated to sexuality, possibly including adult material but excluding educational material')
    sexualityeducation = models.BooleanField(default=False, help_text='	Sites relating to educational information about sexuality.')
    shopping = models.BooleanField(default=False, help_text='Shopping sites')
    socialnetworking = models.BooleanField(default=False, help_text='Social networking websites')
    sportnews = models.BooleanField(default=False, help_text='Sport news sites')
    sports = models.BooleanField(default=False, help_text='All sport sites')
    spyware = models.BooleanField(default=False, help_text='Sites who run or have spyware software to download')
    updatesites = models.BooleanField(default=False, help_text='Sites where software updates are downloaded from including virus sigs')
    vacation = models.BooleanField(default=False, help_text='Sites about going on holiday')
    violence = models.BooleanField(default=False, help_text='Sites containing violence')
    virusinfected = models.BooleanField(default=False, help_text='Sites who host virus infected files')
    warez = models.BooleanField(default=False, help_text='Sites with illegal pirate software')
    weather = models.BooleanField(default=False, help_text='Weather news sites and weather related')
    weapons = models.BooleanField(default=False, help_text='Sites detailing or selling weapons')
    webmail = models.BooleanField(default=False, help_text='Just webmail sites')
    whitelist = models.BooleanField(default=False, help_text='Contains site specifically 100% suitable for kids')

    class Meta:
        verbose_name_plural = "Web Content Filter"

    def __unicode__(self):
        return 'Categories'

    def save(self, *args, **kwargs):
        super(WebContentFilter, self).save(*args, **kwargs)
        self.update_wcf()

    def update_wcf(self):
        categories = WebContentFilter.objects.all().values()[0]
        dg_domain_file = open(settings.DG_DOMAIN, 'w')
        for item in range(1, len(categories)):
            if categories.values()[item] is True:
                dg_domain_buffer = '.Include</etc/dansguardian/lists/blacklists/%s/domains>\n' % (categories.keys()[item])
                dg_domain_file.write(str(dg_domain_buffer+'\n'))
        dg_domain_file.close()
        dg_url_file = open(settings.DG_URL, 'w')
        for item in range(1, len(categories)):
            if categories.values()[item] is True:
                dg_url_buffer = '.Include</etc/dansguardian/lists/blacklists/%s/urls>\n' % (categories.keys()[item])
                dg_url_file.write(str(dg_url_buffer+'\n'))
        dg_url_file.close()


def update_squid():
    proxy_conf = open(settings.SQUID_CONF, 'w')
    squid_conf = 'http_port 127.0.0.1:3128\n' \
                 'http_port 127.0.0.1:3129 intercept\n' \
                 'cache_dir aufs /var/cache/squid3 1024 32 256\n' \
                 'logformat squid_mysql %ts.%03tu %6tr %>a %Ss >Hs %<st %rm %ru %un %Sh %<A %mt' \
                 'access_log daemon:/localhost/aron/access_log/aron/PasswordOfFantasy squid_mysql' \
                 'logfile_daemon /usr/lib/squid3/logfile-daemon_mysql.pl' \
                 'coredump_dir /var/cache/squid3\n' \
                 'refresh_pattern ^ftp:             1440    20%     10080\n' \
                 'refresh_pattern ^gopher:  1440    0%      1440\n' \
                 'refresh_pattern -i (/cgi-bin/|\?) 0       0%      0\n' \
                 'refresh_pattern .         0       20%     4320\n' \
                 'acl localnet src fc00::/7\n' \
                 'acl localnet src fe80::/10\n' \
                 'acl classes_internet src "/etc/squid3/classes_allow"\n' \
                 'acl mac_internet arp "/etc/squid3/mac_allow"\n' \
                 'acl SSL_ports port 443\n' \
                 'acl Safe_ports port 80\n' \
                 'acl Safe_ports port 21\n' \
                 'acl Safe_ports port 443\n' \
                 'acl Safe_ports port 70\n' \
                 'acl Safe_ports port 210\n' \
                 'acl Safe_ports port 1025-65535\n' \
                 'acl Safe_ports port 280\n' \
                 'acl Safe_ports port 488\n' \
                 'acl Safe_ports port 591\n' \
                 'acl Safe_ports port 777\n' \
                 'acl CONNECT method CONNECT\n' \
                 'http_access deny !Safe_ports\n' \
                 'http_access deny CONNECT !SSL_ports\n' \
                 'http_access allow localhost manager\n' \
                 'http_access deny manager\n' \
                 'http_access allow localnet\n' \
                 'http_access allow localhost\n' \
                 'http_access allow classes_internet\n' \
                 'http_access allow mac_internet\n' \
                 'http_access deny all\n' \
                 'visible_hostname firewall\n' \
                 'follow_x_forwarded_for allow all\n' \
                 'forwarded_for on\n' \
                 'always_direct allow all\n' \
                 'pinger_enable off\n' \
                 'shutdown_lifetime 3600.0'
    file_ip_group_allow = open(settings.SQUID_DIR + 'classes_allow', 'w')
    internet_yes = IP.objects.all().filter(classi=Classi.objects.all().filter(internet=True))
    for i in range(0, internet_yes.count()):
        file_ip_group_allow.write(str(internet_yes[i])+'\n')
    file_ip_group_allow.close()
    file_mac_group_allow = open(settings.SQUID_DIR + 'mac_allow', 'w')
    internet_yes = MAC.objects.all().filter(classi=Classi.objects.all().filter(internet=True))
    for i in range(0, internet_yes.count()):
        file_mac_group_allow.write(str(internet_yes[i])+'\n')
    file_mac_group_allow.close()
    proxy_conf.write(squid_conf)
    proxy_conf.close()
    os.system("sudo /etc/init.d/squid3 restart")


class NewDevices(models.Model):
    data_import = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.data_import)

    class Meta:
        verbose_name_plural = "Dispositivi nuovi"

    def new_devices(self):
        try:
            count = 0
            proc = subprocess.Popen('sudo arp -a | egrep eth1 | cut -d" " -f2,4', shell=True, stdout=subprocess.PIPE)
            for line in proc.stdout:
                item = line.split()
                if IP.objects.filter(ip=item[0][1:-1]).exists():
                    pass
                else:
                    ip = IP(ip=item[0][1:-1], classi_id=1)
                    ip.save()
                    count += 1
                if MAC.objects.filter(mac=item[1]).exists():
                    pass
                else:
                    mac = MAC(mac=item[1], classi_id=1)
                    mac.save()
                    count += 1
            if count > 0:
                NewDevices.objects.create()
            proc.wait()
            return count
        except:
            return count

    new_devices.short_description = 'Aggiunto/i'
