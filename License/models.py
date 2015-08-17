from __future__ import unicode_literals
from django.db import models
from ava import key
import datetime
import os

class License(models.Model):
    req = models.CharField(max_length=64, help_text="Richiesta di codice licenza")
    lic = models.CharField(max_length=64, help_text="Attivazione licenza")
    exp_lic = models.DateField('Scandenza licenza', auto_now=True, default=datetime.date.today)

    def __str__(self):
        return self.lic

    def lic_req(self):
        req_key = key.generate_keypair()
        k = key.key_to_string(req_key[0])
        return k

    lic_req.short_description = 'Richiesta di codice licenza'

    request_license = property(lic_req)

    UUID = os.system("ls -lh /dev/disk/by-uuid/ | egrep 'dm-1' | awk '{print $9}'")
    # IDX = key.gen_random_key(UUID)
