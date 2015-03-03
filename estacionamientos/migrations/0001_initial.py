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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('propietario', models.CharField(help_text='Nombre Propio', max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono3', models.CharField(blank=True, max_length=30, null=True)),
                ('email1', models.EmailField(blank=True, max_length=75, null=True)),
                ('email2', models.EmailField(blank=True, max_length=75, null=True)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('apertura', models.TimeField(blank=True, null=True)),
                ('cierre', models.TimeField(blank=True, null=True)),
                ('nroPuesto', models.IntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(max_digits=256, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.ForeignKey(to='estacionamientos.Reserva'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHoraPico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
