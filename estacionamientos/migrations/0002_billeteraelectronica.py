# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BilleteraElectronica',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('idBilletera', models.CharField(max_length=30)),
                ('PIN', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=50)),
                ('CI', models.CharField(max_length=10)),
                ('reserva', models.ForeignKey(to='estacionamientos.Reserva')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
