# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=12)),
                ('tel', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='email1',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='email2',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='propietario',
            field=models.CharField(max_length=50),
        ),
    ]
