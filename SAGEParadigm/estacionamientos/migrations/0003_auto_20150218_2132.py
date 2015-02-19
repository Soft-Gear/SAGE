# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20150216_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='apertura',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='cierre',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='reservasCierre',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='reservasInicio',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
