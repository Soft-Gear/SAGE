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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('propietario', models.CharField(max_length=50, help_text='Nombre Propio')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(null=True, blank=True, max_length=30)),
                ('telefono2', models.CharField(null=True, blank=True, max_length=30)),
                ('telefono3', models.CharField(null=True, blank=True, max_length=30)),
                ('email1', models.EmailField(null=True, blank=True, max_length=75)),
                ('email2', models.EmailField(null=True, blank=True, max_length=75)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('tarifa', models.DecimalField(max_digits=256, null=True, blank=True, decimal_places=2)),
                ('apertura', models.TimeField(null=True, blank=True)),
                ('cierre', models.TimeField(null=True, blank=True)),
                ('reservasInicio', models.TimeField(null=True, blank=True)),
                ('reservasCierre', models.TimeField(null=True, blank=True)),
                ('nroPuesto', models.IntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
