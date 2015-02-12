# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, Reserva, TarifaMinuto,\
    TarifaHorayFraccion, TarifaHora

admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(TarifaHora)
admin.site.register(TarifaMinuto)
admin.site.register(TarifaHorayFraccion)