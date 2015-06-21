# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time,datetime
from estacionamientos.controller import consultar_ingresos
from estacionamientos.models import (
                                        Pago,
                                        Estacionamiento,
                                        Propietario,
                                        Reserva
                                    )

###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class consultaReservaTestCase(TestCase):
    
    #TDD
    def test_sin_estacionamiento(self):
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == total )

    # TDD
    def test_estacionamiento_sin_pagos(self):
        pro = Propietario(
            nombre = "Pepe",
            ci = 'V-12345678',
            tel = "0412-1234567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre      = "nom",
            direccion   = "dir",
            rif         = "J-123456789",
            capacidad   = 20,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == 0)

    # TDD
    def test_un_estacionamiento_un_pago(self):
        pro = Propietario(
            nombre = "Pepe",
            ci = 'V-12345678',
            tel = "0412-1234567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre      = "nom",
            direccion   = "dir",
            rif         = "J-123456789",
            capacidad   = 20,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        r = Reserva(
                estacionamiento = e,
                inicioReserva = datetime(2015,3,10,3,0),
                finalReserva  = datetime(2015,3,10,5,0)
            )
        r.save()
        p = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = "V-1234567",
                tipoPago      = "VISTA",
                reserva          = r,
                monto            = 150,
            )
        p.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == 150)
    # TDD malicia
    def test_un_estacionamiento_muchos_pagos(self):
        n = 1000
        pro = Propietario(
            nombre = "Pepe",
            ci = 'V-12345678',
            tel = "0412-1234567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre      = "nom",
            direccion   = "dir",
            rif         = "J-123456789",
            capacidad   = n,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e.save()
        for i in range(0,n):
            r = Reserva(
                    estacionamiento = e,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0)
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tipoPago      = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == n*100)

    # malicia
    def test_dos_estacionamiento_muchos_pagos(self):
        n  = 1000
        pro1 = Propietario(
            nombre = "PepeUn",
            ci = 'V-12345678',
            tel = "0412-1234567"
        )
        pro1.save()
        e1 = Estacionamiento(
            ci_propietario = pro1,
            nombre      = "nom1",
            direccion   = "dir1",
            rif         = "J-123456789",
            capacidad   = n,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        pro2 = Propietario(
            nombre = "PepeDos",
            ci = 'V-12345679',
            tel = "0412-1234568"
        )
        pro2.save()
        e2 = Estacionamiento(
            ci_propietario = pro2,
            nombre      = "nom2",
            direccion   = "dir3",
            rif         = "J-19876543321",
            capacidad   = n,
            apertura    = time(0,0),
            cierre      = time(23,59),
        )
        e1.save()
        e2.save()
        for i in range(0,n):
            r = Reserva(
                    estacionamiento = e1,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0)
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tipoPago         = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()
        for i in range(0,n):
            r = Reserva(
                    estacionamiento = e2,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0)
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tipoPago         = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()
        lista, total = consultar_ingresos("J-123456789")
        lista2, total2 = consultar_ingresos("J-19876543321")
        self.assertTrue(len(lista) == 1 and total == n*100)
        self.assertTrue(len(lista2) == 1 and total2 == n*100)

    def test_muchos_estacionamiento_con_disintos_rif(self):
        n  = 1000
        for i in range(0,n):
            pro = Propietario(
                nombre = "prop%d"%i,
                ci = 'V-12345678%d'%i,
                tel = "0412-1234567"
            )
            pro.save()    
            e1 = Estacionamiento(
                ci_propietario = pro,
                nombre      = "nom%d"%i,
                direccion   = "dir1",
                rif         = "J-%i"%(123456789-i),
                capacidad   = n,
                apertura    = time(0,0),
                cierre      = time(23,59),
            )
            e1.save()
            r = Reserva(
                    estacionamiento = e1,
                    inicioReserva = datetime(2015,3,10,3,0),
                    finalReserva  = datetime(2015,3,10,5,0)
                )
            r.save()
            p = Pago(
                    fechaTransaccion = datetime.now(),
                    cedula           = "V-1234567",
                    tipoPago         = "VISTA",
                    reserva          = r,
                    monto            = 100,
                )
            p.save()
        lista, total = consultar_ingresos("J-123456789")
        self.assertTrue(len(lista) == 1 and total == 100)

