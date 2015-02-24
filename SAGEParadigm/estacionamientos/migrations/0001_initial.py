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
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('propietario', models.CharField(help_text='Nombre Propio', max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(max_length=30, null=True, blank=True)),
                ('telefono2', models.CharField(max_length=30, null=True, blank=True)),
                ('telefono3', models.CharField(max_length=30, null=True, blank=True)),
                ('email1', models.EmailField(max_length=75, null=True, blank=True)),
                ('email2', models.EmailField(max_length=75, null=True, blank=True)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('tarifa', models.DecimalField(null=True, max_digits=256, decimal_places=2, blank=True)),
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
            name='Pago',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('tarjeta', models.CharField(max_length=16)),
                ('monto', models.DecimalField(max_digits=256, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.ForeignKey(to='estacionamientos.Reserva'),
            preserve_default=True,
        ),
    ]
