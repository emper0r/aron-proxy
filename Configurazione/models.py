from django.db import models
from License import bf
from web import settings
import gzip
import os


class ImportConfig(models.Model):
    filename = models.FileField('File di configurazione', upload_to='.', null=True, max_length=20)

    def __str__(self):
        return self.filename.name

    class Meta:
        verbose_name_plural = "Importa"


class ExportConfig(models.Model):
    def config(self):
        tmp_sql = '/tmp/._.sql'
        os.system('mysqldump -u %s -h %s --password=%s %s --ignore-table=%s.aron_logs > %s' %
                  (settings.DATABASES.values()[0]['USER'],
                   settings.DATABASES.values()[0]['HOST'],
                   settings.DATABASES.values()[0]['PASSWORD'],
                   settings.DATABASES.values()[0]['NAME'],
                   settings.DATABASES.values()[0]['NAME'],
                   tmp_sql))

        file_save = gzip.open('/tmp/config.aron.prx', 'wb')
        file_save.write(bf.crypt(open(tmp_sql, 'r').read()))
        file_save.close()
        os.unlink(tmp_sql)
        os.system("sudo mv /tmp/config.aron.prx %s/" % settings.STATICFILES_DIRS)
        return "<a href=\"../../../static/config.aron.prx\">config.aron.prx</a>"

    config.allow_tags = True
    config.description = 'Scarica'

    class Meta:
        verbose_name_plural = "Esporta"
