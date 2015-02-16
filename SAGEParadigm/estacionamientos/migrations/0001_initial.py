# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('propietario', models.CharField(help_text='Nombre Propio', max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(max_length=30, blank=True, null=True)),
                ('telefono2', models.CharField(max_length=30, blank=True, null=True)),
                ('telefono3', models.CharField(max_length=30, blank=True, null=True)),
                ('email1', models.EmailField(max_length=75, blank=True, null=True)),
                ('email2', models.EmailField(max_length=75, blank=True, null=True)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('tarifa', models.CharField(max_length=50, blank=True, null=True)),
                ('apertura', models.TimeField(blank=True, null=True)),
                ('cierre', models.TimeField(blank=True, null=True)),
                ('reservasInicio', models.TimeField(blank=True, null=True)),
                ('reservasCierre', models.TimeField(blank=True, null=True)),
                ('nroPuesto', models.IntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('inicioReserva', models.TimeField()),
                ('finalReserva', models.TimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
