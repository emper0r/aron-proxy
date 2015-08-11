# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professori',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ip',
            options={'verbose_name_plural': 'Gestione - IP'},
        ),
        migrations.AlterModelOptions(
            name='mac',
            options={'verbose_name_plural': 'Gestione - MAC'},
        ),
        migrations.AlterModelOptions(
            name='webcontentfilter',
            options={'verbose_name_plural': 'Gestione - Web Content Filter'},
        ),
        migrations.AlterField(
            model_name='classi',
            name='group',
            field=models.CharField(help_text='Obbligatorio. Identificativo della Classe', unique=True, max_length='20', verbose_name='Nome della Classe'),
        ),
        migrations.AddField(
            model_name='professori',
            name='group',
            field=models.OneToOneField(to='aron.Classi'),
        ),
        migrations.AddField(
            model_name='professori',
            name='professori',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
