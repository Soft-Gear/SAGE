# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Propietario, Estacionamiento, Reserva, Pago, TarifaMinuto,\
    TarifaHorayFraccion, TarifaHora, BilleteraElectronica, Pago_billetera,\
    Recarga_billetera

admin.site.register(Propietario)
admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(BilleteraElectronica)
admin.site.register(Recarga_billetera)
admin.site.register(TarifaHora)
admin.site.register(TarifaMinuto)
admin.site.register(TarifaHorayFraccion)
