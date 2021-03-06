# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Propietario, Estacionamiento, Reserva, Pago, TarifaMinuto,\
    TarifaHorayFraccion, TarifaHora, BilleteraElectronica, HistorialBilleteraElectronica, SAGE

admin.site.register(SAGE)
admin.site.register(Propietario)
admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(BilleteraElectronica)
admin.site.register(HistorialBilleteraElectronica)
admin.site.register(TarifaHora)
admin.site.register(TarifaMinuto)
admin.site.register(TarifaHorayFraccion)
