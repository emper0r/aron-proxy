# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aron', '0002_auto_20150811_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professori',
            name='group',
        ),
        migrations.RemoveField(
            model_name='professori',
            name='professori',
        ),
        migrations.AddField(
            model_name='professori',
            name='professori',
            field=models.ManyToManyField(to='aron.Classi'),
        ),
    ]
