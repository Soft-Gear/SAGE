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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('apertura', models.TimeField(null=True, blank=True)),
                ('cierre', models.TimeField(null=True, blank=True)),
                ('nroPuesto', models.IntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(null=True, to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=10)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=10)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHoraPico',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=10)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=10)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=10)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
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
