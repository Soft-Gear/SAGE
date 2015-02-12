# -*- coding: utf-8 -*-

import datetime
from django.test import Client
from django.test import TestCase
import unittest

from estacionamientos.controller import *
from estacionamientos.forms import *
from estacionamientos.models import *
from estacionamientos.forms import *
from estacionamientos.models import TarifaMinuto,TarifaHora,TarifaHorayFraccion


###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class SimpleTest(unittest.TestCase):
    # normal
    def setUp(self):
        self.client = Client()

    # normal
    def test_primera(self):
        response = self.client.get('/estacionamientos/')
        self.assertEqual(response.status_code, 200)



###################################################################
#                    ESTACIONAMIENTO_ALL FORM
###################################################################

class SimpleFormTestCase(TestCase):

    # malicia
    def test_CamposVacios(self):
        form_data = {}
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_SoloUnCampoNecesario(self):
        form_data = {
            'propietario': 'Pedro'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_DosCamposNecesarios(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_TresCamposNecesarios(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_TodosLosCamposNecesarios(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_PropietarioInvalidoDigitos(self):
        form_data = {
            'propietario': 'Pedro132',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_PropietarioInvalidoSimbolos(self):
        form_data = {
            'propietario': 'Pedro!',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_RIFtamanoinvalido(self):
        form_data = {
            'propietario': 'Pedro132',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V1234567'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_RIFformatoinvalido(self):
        form_data = {
            'propietario': 'Pedro132',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'Kaa123456789'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_AgregarTLFs(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789',
            'telefono_1': '02129322878',
            'telefono_2': '04149322878',
            'telefono_3': '04129322878'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_FormatoInvalidoTLF(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789',
            'telefono_1': '02119322878'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_TamanoInvalidoTLF(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789',
            'telefono_1': '0219322878'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_AgregarCorreos(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789',
            'telefono_1': '02129322878',
            'telefono_2': '04149322878',
            'telefono_3': '04129322878',
            'email_1': 'adminsitrador@admin.com',
            'email_2': 'usua_rio@users.com'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_CorreoInvalido(self):
        form_data = {
            'propietario': 'Pedro',
            'nombre': 'Orinoco',
            'direccion': 'Caracas',
            'rif': 'V123456789',
            'telefono_1': '02129322878',
            'telefono_2': '04149322878',
            'telefono_3': '04129322878',
            'email_1': 'adminsitrador@a@dmin.com'
        }
        form = EstacionamientoForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

class ExtendedFormTestCase(TestCase):

    # malicia
    def test_EstacionamientoExtendedForm_UnCampo(self):
        form_data = { 'puestos': 2}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_DosCampos(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_TresCampos(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_CuatroCampos(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_EstacionamientoExtendedForm_CincoCampos(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_EstacionamientoExtendedForm_TodosCamposBien(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # caso borde
    def test_EstacionamientoExtendedForm_Puestos0(self):
        form_data = { 'puestos': 0,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # caso borde
    def test_EstacionamientoExtendedForm_HoraInicioIgualHoraCierre(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(6, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # caso borde
    def test_EstacionamientoExtendedForm_HoraIniReserIgualHoraFinReser(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(7, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_EstacionamientoExtendedForm_StringEnPuesto(self):
        form_data = { 'puestos': 'hola',
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_StringHoraInicio(self):
        form_data = { 'puestos': 2,
                                'horarioin': 'holaa',
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
        form_data = { 'puestos': 2,
                                'horarioin':-1,
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_NoneEntarifa(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': None}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
        form_data = { 'puestos': 2,
                                'horarioin': 'holaa',
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': None,
                                'horario_reserout': datetime.time(14, 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
        form_data = { 'puestos': 2,
                                'horarioin': datetime.time(6, 0),
                                'horarioout': datetime.time(19, 0),
                                'horario_reserin': datetime.time(7, 0),
                                'horario_reserout': [datetime.time(14, 0)],
                                'tarifa': 12}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
###################################################################

class ExtendedFormControllerTestCase(TestCase):
    # normal
    def test_HorariosValidos(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (True, ''))

    # malicia
    def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 11, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

    # caso borde
    def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

    # caso borde
    def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

    # caso borde
    def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 12, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

    # caso borde
    def test_Limite_HorarioValido_Apertura_Cierre(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 12, minute = 0, second = 1)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 12, minute = 0, second = 1)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (True, ''))

    # caso borde
    def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
        HoraInicio = datetime.time(hour = 0, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 23, minute = 59, second = 59)
        ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 23, minute = 59, second = 59)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (True, ''))

    # caso borde
    def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

    # caso borde
    def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

    # malicia
    def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 17, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas'))

    # malicia
    def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
        HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
        HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
        ReservaInicio = datetime.time(hour = 10, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertura del estacionamiento'))



###################################################################
# ESTACIONAMIENTO_RESERVA_FORM
###################################################################

class ReservaFormTestCase(TestCase):
    # malicia
    def test_EstacionamientoReserva_Vacio(self):
        form_data = {}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_EstacionamientoReserva_UnCampo(self):
        form_data = {'inicio':datetime.time(6, 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # normal
    def test_EstacionamientoReserva_TodosCamposBien(self):
        form_data = {'inicio':datetime.time(6, 0), 'final':datetime.time(12, 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_EstacionamientoReserva_InicioString(self):
        form_data = {'inicio':'hola',
                                'final':datetime.time(12, 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoReserva_FinString(self):
        form_data = {'inicio':datetime.time(6, 0),
                                'final':'hola'}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoReserva_InicioNone(self):
        form_data = {'inicio':None,
                                'final':datetime.time(12, 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoReserva_finalNone(self):
        form_data = {'inicio':datetime.time(6, 0),
                                'final':None}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

###################################################################
# PRUEBAS DE FUNCIONES DEL CONTROLADOR
###################################################################

##############################################################
# Estacionamiento Reserva Controlador
###################################################################

class ReservaFormControllerTestCase(TestCase):
# HorarioReserva, pruebas Unitarias
    # normal
    def test_HorarioReservaValido(self):
        ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 15, minute = 0, second = 0)
        HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
        HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (True, ''))

    # caso borde
    def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
        ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 12, minute = 59, second = 59)
        HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
        HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

    # caso borde
    def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
        ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 13, minute = 59, second = 59)
        HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
        HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora'))

    # caso borde
    def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
        ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
        ReservaFin = datetime.time(hour = 18, minute = 0, second = 1)
        HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
        HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe estar en un horario válido'))

    # caso borde
    def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
        ReservaInicio = datetime.time(hour = 11, minute = 59, second = 59)
        ReservaFin = datetime.time(hour = 15, minute = 0, second = 1)
        HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
        HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de cierre de reserva debe estar en un horario válido'))

    # malicia
    def test_Reservacion_CamposVacios(self):
        form_data = {'inicio':datetime.time(6, 0), 'final':datetime.time(12, 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), True)

###############################################################################
# Marzullo
###############################################################################

from estacionamientos.controller import marzullo
from estacionamientos.models import Estacionamiento, Reserva
from datetime import time

class TestMarzullo(unittest.TestCase):
    def crearEstacionamiento(self, puestos):
        e = Estacionamiento(
            propietario = "prop",
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            nroPuesto = puestos
        )
        e.save()
        return e

    def testOneReservation(self): #borde
        e = self.crearEstacionamiento(1)
        self.assertTrue(marzullo(e.id, time(9), time(15)))

    def testNoSpotParking(self): #borde
        e = self.crearEstacionamiento(0)
        self.assertFalse(marzullo(e.id, time(9), time(15)))

    def testTenSpotsOneReservation(self): #malicia
        e = self.crearEstacionamiento(10)
        self.assertTrue(marzullo(e.id, time(9), time(15)))

    def testAddTwoReservation(self): #malicia
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="18:00").save()
        self.assertTrue(marzullo(e.id, time(12), time(18)))

    def testAddThreeReservations(self): #malicia
        e = self.crearEstacionamiento(3)
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        self.assertTrue(marzullo(e.id, time(12), time(18)))

    def testFiveSpotsFiveReservation(self): #Borde
        e = self.crearEstacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="12:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        self.assertTrue(marzullo(e.id, time(10), time(18)))

    def testFiveSpotsSixReservation(self): #borde
        e = self.crearEstacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="12:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="12:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="18:00").save()
        self.assertFalse(marzullo(e.id, time(9), time(18)))
        self.assertFalse(marzullo(e.id, time(9), time(15)))

    def testFiveSpotsSixReservationNoOverlapping(self): #esquina
        e = self.crearEstacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="12:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="12:00", finalReserva="18:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="18:00").save()
        self.assertTrue(marzullo(e.id, time(6), time(10)))
        self.assertTrue(marzullo(e.id, time(9), time(12)))

    def testManyReservationsMaxOverlapping(self): #malicia
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="07:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="08:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="07:00", finalReserva="11:00").save()
        Reserva(estacionamiento = e, inicioReserva="08:00", finalReserva="12:00").save()
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="13:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="09:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        Reserva(estacionamiento = e, inicioReserva="10:00", finalReserva="15:00").save()
        self.assertTrue(marzullo(e.id, time(10), time(15)))

    def testManyReservationsOneOverlap(self): #malicia y esquinas
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="07:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="08:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="07:00", finalReserva="11:00").save()
        Reserva(estacionamiento = e, inicioReserva="08:00", finalReserva="12:00").save()
        Reserva(estacionamiento = e, inicioReserva="09:00", finalReserva="13:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="09:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        Reserva(estacionamiento = e, inicioReserva="06:00", finalReserva="10:00").save()
        self.assertFalse(marzullo(e.id, time(9), time(10)))

class RateTestCase(TestCase):
	
	#Pruebas para tarifa de hora y fraccion
		
	def test_oneHourFraccionPay(self):
		initial_time = datetime.time(13,0)
		final_time = datetime.time(14,0)
		rate = TarifaHorayFraccion(tarifa = 2)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)
		
	def test_twoHourFraccionPay(self):
		initial_time = datetime.time(13,0)
		final_time = datetime.time(15,0)
		rate = TarifaHorayFraccion(tarifa = 2)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),4)
		
	def test_halfHourFraccionPay(self):
		initial_time = datetime.time(13,15)
		final_time = datetime.time(13,45)
		rate = TarifaHorayFraccion(tarifa = 2)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)
		
	def test_onePlusHalfHourFraccionPay(self):
		initial_time = datetime.time(13,0)
		final_time = datetime.time(14,30)
		rate = TarifaHorayFraccion(tarifa = 20)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),30)
		
	def test_DecimalFraccionPay(self):
		initial_time = datetime.time(19,0)
		final_time = datetime.time(20,15)
		rate = TarifaHorayFraccion(tarifa = 1)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),1.5)
		
	def test_onePlusHalfPlusMinuteHourFraccionPay(self):
		initial_time = datetime.time(15,15)
		final_time = datetime.time(16,46)
		rate = TarifaHorayFraccion(tarifa = 2)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),4)
		
	def test_oneDayFraccionPay(self):
		initial_time = datetime.time(0,0)
		final_time = datetime.time(23,59)
		rate = TarifaHorayFraccion(tarifa = 2)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),48)
		
	# Pruebas para la tarifa por minuto
	
	def test_oneMinutePay(self):
		initial_time = datetime.time(15,1)
		final_time = datetime.time(15,2)
		rate = TarifaMinuto(tarifa = 80)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),80)
		
	def test_twoMinutePay(self):
		initial_time = datetime.time(15,1)
		final_time = datetime.time(15,3)
		rate = TarifaMinuto(tarifa = 80)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),160)
		
	def test_oneDayMinutePay(self):
		initial_time = datetime.time(0,0)
		final_time = datetime.time(23,59)
		rate = TarifaMinuto(tarifa = 1)
		self.assertEqual(rate.calcularPrecio(initial_time,final_time),1439)

	# Pruebas para la clase tarifa	

	def test_OneHourRate(self):
		rate = TarifaHora(tarifa = 800)
		initial_datetime = datetime.time(13,0)
		final_datetime = datetime.time(14,0)
		value = rate.calcularPrecio(initial_datetime, final_datetime)
		self.assertEquals(value, 800)
		
	def test_MoreThanHourRate(self):
		rate = TarifaHora(tarifa = 800)
		initial_datetime = datetime.time(6,8)
		final_datetime = datetime.time(7,9)
		value = rate.calcularPrecio(initial_datetime, final_datetime)
		self.assertEquals(value, 1600)
		
	def test_LessThanAnHour(self):
		rate = TarifaHora(tarifa = 800)
		initial_datetime = datetime.time(11,0)
		final_datetime = datetime.time(11,15)
		value = rate.calcularPrecio(initial_datetime, final_datetime)
		self.assertEquals(value, 800)
		
	def testCompleteDay(self):
		rate=TarifaHora(tarifa=1)
		initial_time=datetime.time(0,0)
		final_time=datetime.time(23,59)
		value = rate.calcularPrecio(initial_time, final_time)
		self.assertEqual(value, 24)
