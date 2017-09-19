from __future__ import unicode_literals
from django.db import models
from django.db.models import signals
from django.conf import settings
import os
from License import bf
import MySQLdb


class Routing(models.Model):
    db = MySQLdb.connect(settings.DATABASES.values()[0]['HOST'],
                             settings.DATABASES.values()[0]['USER'],
                             settings.DATABASES.values()[0]['PASSWORD'],
                             settings.DATABASES.values()[0]['NAME'])
    cursor = db.cursor()
    mode = "SELECT mode FROM Routing_routing;"
    cursor.execute(mode)
    actual_mode = cursor.fetchone()
    CHOICES = ()
    if str(actual_mode[0]) == 'Routing':
        CHOICES = (('Proxy/Classes', 'Proxy/Classes'),)
    if str(actual_mode[0]) == 'Proxy/Classes':
        CHOICES = (('Routing', 'Routing'),)
    mode = models.CharField("Sceglie\'",
                            choices=CHOICES,
                            max_length=13,
                            blank=False,
                            null=False,
                            help_text='Selezzione il modo di lavorare l\'Aron Proxy')

    class Meta:
        verbose_name_plural = "Funzionalita'"

    def __unicode__(self):
        return unicode(self.mode)


def reload_web(sender, instance, created, **kwargs):
    os.system("sudo /etc/init.d/apache2 reload")

signals.post_save.connect(reload_web, sender=Routing)
