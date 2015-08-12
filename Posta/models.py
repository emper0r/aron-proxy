from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import os


class VeximDomains(models.Model):
    DOMAIN_TYPES = (
        ('local', 'Local'),
        ('relay', 'Relay')
    )
    domain = models.CharField('Dominio',
                              max_length=128,
                              unique=True,
                              help_text='Dominio virtuale di Posta Elettronica')
    enabled = models.BooleanField(default=True)
    maxmsgsize = models.IntegerField('Massima misura del messagio',
                                     default=settings.VEXIM_MAXMSGSIZE,
                                     help_text='Misura del messaggio in MegaBytes')
    max_accounts = models.IntegerField(default=0,
                                       help_text='Massimo di account disponibili per questo dominio. '
                                                            'Il zero definici ilimitato.')
    type = models.CharField('Tipo Dominio',
                            max_length=5,
                            choices=DOMAIN_TYPES,
                            default='local',
                            help_text='Tipo di dominio Local o Relay')
    avscan = models.BooleanField('Antivirus',
                                 default=False,
                                 help_text='Abilitare Antivirus')
    spamassassin = models.BooleanField('Anti SPAM',
                                       default=False,
                                       help_text='Abilitare Spamassassin')
    mailinglists = models.BooleanField('Lista distribuzioni',
                                       default=False,
                                       help_text='Abilitare Lista distribuzioni')
    sa_tag = models.IntegerField('Score AntiSpam Minimo',
                                 default=settings.VEXIM_SA_TAG,
                                 help_text='Score minimo per controllo Spamassasin')
    sa_refuse = models.IntegerField('Score AntiSpam Massimo',
                                    default=settings.VEXIM_SA_REFUSE,
                                    help_text='Score massimo per controllo Spamassasin')
    maildir = models.CharField(max_length=128,
                               default=settings.VEXIM_MAILHOME)
    uid = models.IntegerField(default=settings.VEXIM_UID)
    gid = models.IntegerField(default=settings.VEXIM_GID)
    blocklists = models.BooleanField(default=False)
    complexpass = models.BooleanField(default=False)
    pipe = models.BooleanField(default=True)

    def __unicode__(self):
        return self.domain

    class Meta:
        verbose_name_plural = "Posta - Dominio"

    def save(self, *args, **kwargs):
        self.maildir = settings.VEXIM_MAILHOME + self.domain
        if not os.path.exists(self.maildir):
            os.makedirs(self.maildir)
            os.chown(self.maildir, 750)
        # self.maxmsgsize = self.maxmsgsize * 1024 * 1024
        super(VeximDomains, self).save(*args, **kwargs)

class VeximUsers(models.Model):
    # USER_TYPES = (
    #     ('local', 'Local user'),
    #     ('admin', 'Domain admin'),
    #     ('alias', 'Alias'),
    #     ('catchall', 'Catchall'),
    #     ('fail', 'Blackholed address'),
    #     ('pipe', 'System pipe')
    # )
    user = models.OneToOneField(User)
    domain = models.ForeignKey(VeximDomains)
    passwd = models.CharField(max_length=64)
    localpart = models.EmailField(max_length=64,
                                  help_text='Indirizzo mail del dominio selezzionato')
    on_avscan = models.BooleanField('Antivirus',
                                    default=True,
                                    help_text='Abilitare Antivirus')
    on_spamassassin = models.BooleanField('AntiSPAM',
                                          default=True)
    on_forward = models.BooleanField('Attivazione Inoltro',
                                     default=False,
                                     help_text='Inoltra mail un\'altro indirizzo')
    forward = models.EmailField('Indirizzo mail inoltro',
                                max_length=32,
                                blank=True)
    unseen = models.BooleanField('Posta non visibile',
                                 default=False,
                                 help_text='Indirizzo mail cego')
    on_vacation = models.BooleanField('Vacanze',
                                      default=False,
                                      help_text='Abilitare vacance')
    vacation = models.TextField('Testo ferie',
                                blank=True,
                                help_text='Scrivi il messaggio delle vacanze')
    maxmsgsize = models.IntegerField('Massima misura del messaggio.',
                                     default=settings.VEXIM_MAXMSGSIZE,
                                     help_text='Massima misura del messaggio in bytes')
    quota = models.IntegerField(default=1073741824,
                                help_text='Massima misura della casella in bytes')
    sa_tag = models.IntegerField('SPAM Assassin Minimo',
                                 default=5,
                                 help_text='Score minimo per Spamassassin')
    sa_refuse = models.IntegerField('SPAM Assassin Massimo',
                                    default=10,
                                    help_text='Score minimo per Spamassassin')
    on_blocklist = models.BooleanField(default=False)
    on_complexpass = models.BooleanField(default=False)
    on_piped = models.BooleanField(default=False)
    username = models.CharField('Login',
                                max_length=64,
                                null=False)
    enabled = models.BooleanField(default=True,
                                  help_text='Utente Abilitato')
    uid = models.IntegerField(default=settings.VEXIM_UID)
    gid = models.IntegerField(default=settings.VEXIM_GID)
    # clear
    # password
    smtp = models.CharField(max_length=64)
    pop = models.CharField(max_length=64)
    type = models.CharField(max_length=8,
                            default=settings.VEXIM_TYPE)

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name_plural = "Posta - Account"
