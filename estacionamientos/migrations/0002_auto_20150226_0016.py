# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tarifa2', models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='finEspecial',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='inicioEspecial',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='tarifa2',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='finEspecial',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='inicioEspecial',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='tarifa2',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='finEspecial',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='inicioEspecial',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='tarifa2',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True),
            preserve_default=True,
        ),
    ]
