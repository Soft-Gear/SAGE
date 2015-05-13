# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Propietario, Estacionamiento, Reserva, Pago, TarifaMinuto,\
    TarifaHorayFraccion, TarifaHora

admin.site.register(Propietario)
admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(TarifaHora)
admin.site.register(TarifaMinuto)
admin.site.register(TarifaHorayFraccion)