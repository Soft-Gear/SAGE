# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, Reserva

admin.site.register(Estacionamiento)
admin.site.register(Reserva)