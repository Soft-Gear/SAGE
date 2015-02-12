# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('inicioReserva', models.TimeField()),
                ('finalReserva', models.TimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='reservasmodel',
            name='Estacionamiento',
        ),
        migrations.DeleteModel(
            name='ReservasModel',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Apertura',
            new_name='apertura',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Cierre',
            new_name='cierre',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Email_1',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Email_2',
            new_name='email2',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='NroPuesto',
            new_name='nroPuesto',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Propietario',
            new_name='propietario',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Reservas_Cierre',
            new_name='reservasCierre',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Reservas_Inicio',
            new_name='reservasInicio',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Rif',
            new_name='rif',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Tarifa',
            new_name='tarifa',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Telefono_1',
            new_name='telefono1',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Telefono_2',
            new_name='telefono2',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='Telefono_3',
            new_name='telefono3',
        ),
    ]
