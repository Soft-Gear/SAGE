# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20150512_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='propietario',
            field=models.ForeignKey(to='estacionamientos.Propietario'),
        ),
    ]
