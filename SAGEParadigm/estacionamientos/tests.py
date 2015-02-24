# -*- coding: utf-8 -*-

from datetime import datetime, time
from django.test import Client
from django.test import TestCase
import unittest

from estacionamientos.controller import HorarioEstacionamiento, validarHorarioReserva, marzullo
from estacionamientos.models import Estacionamiento, Reserva
from estacionamientos.forms import EstacionamientoForm, EstacionamientoExtendedForm, EstacionamientoReserva,\
    PagoTarjetaDeCredito
from estacionamientos.models import TarifaMinuto,TarifaHora,TarifaHorayFraccion
from decimal import Decimal


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
                      'horarioin': time(hour = 6,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_TresCampos(self):
        form_data = { 'puestos': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_CuatroCampos(self):
        form_data = { 'puestos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'horario_reserin': time(hour = 7,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_EstacionamientoExtendedForm_CincoCampos(self):
        form_data = { 'puestos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'horario_reserin': time(hour = 7,  minute = 0),
                      'horario_reserout': time( hour = 14,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # caso borde
    def test_EstacionamientoExtendedForm_TodosCamposBien(self):
        form_data = { 'puestos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'horario_reserin': time(hour = 7,  minute = 0),
                      'horario_reserout': time(hour = 14,  minute = 0),
                      'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # caso borde
    def test_EstacionamientoExtendedForm_Puestos0(self):
        form_data = { 'puestos': 0,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'horario_reserin': time(hour = 7,  minute = 0),
                      'horario_reserout': time(hour = 14,  minute = 0),
                      'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # caso borde
    def test_EstacionamientoExtendedForm_HoraInicioIgualHoraCierre(self):
        form_data = { 'puestos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 6,  minute = 0),
                      'horario_reserin': time(hour = 7,  minute = 0),
                      'horario_reserout': time(hour = 14,  minute = 0),
                      'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # caso borde
    def test_EstacionamientoExtendedForm_HoraIniReserIgualHoraFinReser(self):
        form_data = { 'puestos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'horario_reserin': time( hour = 7,  minute = 0),
                      'horario_reserout': time( hour = 7,  minute = 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_EstacionamientoExtendedForm_StringEnPuesto(self):
        form_data = { 'puestos': 'hola',
                                'horarioin': time(hour = 6,  minute = 0),
                                'horarioout': time(hour = 19,  minute = 0),
                                'horario_reserin': time( hour = 7,  minute = 0),
                                'horario_reserout': time( hour = 14,  minute = 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_StringHoraInicio(self):
        form_data = { 'puestos': 2,
                                'horarioin': 'holaa',
                                'horarioout': time(hour = 19,  minute = 0),
                                'horario_reserin': time(hour = 7,  minute = 0),
                                'horario_reserout': time( hour = 14,  minute = 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
        form_data = { 'puestos': 2,
                                'horarioout': time(hour = 19,  minute = 0),
                                'horario_reserin': time( hour = 7,  minute = 0),
                                'horario_reserout': time(hour = 14,  minute = 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_NoneEntarifa(self):
        form_data = { 'puestos': 2,
                                'horarioin': time( hour = 6,  minute = 0),
                                'horarioout': time(hour = 19,  minute = 0),
                                'horario_reserin': time(hour = 7,  minute = 0),
                                'horario_reserout': time( hour = 14,  minute = 0),
                                'tarifa': None}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
        form_data = { 'puestos': 2,
                                'horarioin': 'holaa',
                                'horarioout': time(hour = 19,  minute = 0),
                                'horario_reserin': None,
                                'horario_reserout': time( hour = 14,  minute = 0),
                                'tarifa': '12'}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
        form_data = { 'puestos': 2,
                                'horarioin': time( hour = 6,  minute = 0),
                                'horarioout': time(hour = 19,  minute = 0),
                                'horario_reserin': time(hour = 7,  minute = 0),
                                'horario_reserout': [time( hour = 14,  minute = 0)],
                                'tarifa': 12}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertEqual(form.is_valid(), False)

######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
###################################################################

class ExtendedFormControllerTestCase(TestCase):
    # normal
    def test_HorariosValidos(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 18, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (True, ''))

    # malicia
    def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 11, minute = 0, second = 0)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 18, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

    # caso borde
    def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 12, minute = 0, second = 0)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 18, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

    # caso borde
    def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 11, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

    # caso borde
    def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 12, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

    # caso borde
    def test_Limite_HorarioValido_Apertura_Cierre(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 12, minute = 0, second = 1)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 12, minute = 0, second = 1)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (True, ''))

    # caso borde
    def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
        HoraInicio = time(hour = 0, minute = 0, second = 0)
        HoraFin = time(hour = 23, minute = 59, second = 59)
        ReservaInicio = time(hour = 12, minute = 0, second = 0)
        ReservaFin = time(hour = 23, minute = 59, second = 59)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (True, ''))

    # caso borde
    def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 19, minute = 0, second = 0)
        ReservaFin = time(hour = 20, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

    # caso borde
    def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 19, minute = 0, second = 0)
        ReservaFin = time(hour = 20, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

    # malicia
    def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 17, minute = 0, second = 0)
        ReservaFin = time(hour = 20, minute = 0, second = 0)
        x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
        self.assertEqual(x, (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas'))

    # malicia
    def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
        HoraInicio = time(hour = 12, minute = 0, second = 0)
        HoraFin = time(hour = 18, minute = 0, second = 0)
        ReservaInicio = time(hour = 10, minute = 0, second = 0)
        ReservaFin = time(hour = 11, minute = 0, second = 0)
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
        form_data = {'inicio':datetime(year = 2000, month = 6, day = 15, hour = 6,  minute = 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # normal
    def test_EstacionamientoReserva_TodosCamposBien(self):
        form_data = {'inicio':datetime(year = 2000, month = 6, day = 15, hour = 6,  minute = 0), 'final':datetime(year = 2000, month = 6, day = 15, hour = 12,  minute = 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), True)

    # malicia
    def test_EstacionamientoReserva_InicioString(self):
        form_data = {'inicio':'hola',
                                'final':datetime(year = 2000, month = 6, day = 15, hour = 12,  minute = 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoReserva_FinString(self):
        form_data = {'inicio':datetime(year = 2000, month = 6, day = 15, hour = 6,  minute = 0),
                                'final':'hola'}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoReserva_InicioNone(self):
        form_data = {'inicio':None,
                                'final':datetime(year = 2000, month = 6, day = 15, hour = 12,  minute = 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

    # malicia
    def test_EstacionamientoReserva_finalNone(self):
        form_data = {'inicio':datetime(year = 2000, month = 6, day = 15, hour = 6,  minute = 0),
                                'final':None}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), False)

###################################################################
# Pago Tarjeta de Credito Form
###################################################################
class PagoTarjetaDeCreditoFormTestCase(TestCase):

    # borde
    def test_PagoTarjetaForm_Vacio(self):
        form_data = {}
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_PagoTarjetaForm_UnCampo(self):
        form_data = {
            'nombre': 'Pedro',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_DosCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_TresCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CuatroCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())        

    #borde
    def test_PagoTarjetaForm_CincoCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_PagoTarjetaForm_SeisCampos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '24277076',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertTrue(form.is_valid())

    #borde
    def test_PagoTarjetaForm_NombreInvalidoDigitos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_NombreInvalidoSimbolos(self):
        form_data = {
            'nombre': 'Pedro*',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_ApellidoInvalidoDigitos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez1',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_ApellidoInvalidoSimbolos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': '¡Perez!',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CedulaTipoInvalido(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'J',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_CedulaInvalida(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': 'V12345',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_TipoTarjetaInvalido(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'American',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #borde
    def test_PagoTarjetaForm_TarjetaInvalido(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'V',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': 'ab12345',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PagoTarjetaForm_DosCamposErroneos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'foo',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PagoTarjetaForm_CuatroCamposErroneos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedulaTipo': 'foo',
            'cedula': '12345sda6789',
            'tarjetaTipo': 'American',
            'tarjeta': '1234',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())

    #malicia
    def test_PagoTarjetaForm_TodosCamposErroneos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez2',
            'cedulaTipo': 'foo',
            'cedula': '12345678as9',
            'tarjetaTipo': 'American',
            'tarjeta': 'prueba',
        }
        form = PagoTarjetaDeCredito(data = form_data)
        self.assertFalse(form.is_valid())


##############################################################
# Estacionamiento Reserva Controlador
###################################################################

class ReservaFormControllerTestCase(TestCase):
# HorarioReserva, pruebas Unitarias
    # normal
    '''def test_HorarioReservaValido(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 13, minute = 0, second = 0)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 15, minute = 0, second = 0)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (True, ''))'''

    # caso borde
    def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 13, minute = 0, second = 0)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 12, minute = 59, second = 59)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

    # caso borde
    def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 13, minute = 0, second = 0)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 13, minute = 59, second = 59)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora'))

    # caso borde (18/02/2015): Modificado para el granulado en minutos 
    '''def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 13, minute = 0, second = 0)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 18, minute = 1, second = 0)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de cierre de reserva debe estar en un horario válido'))'''

    # Caso borde 
    '''def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 11, minute = 59, second = 59)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 15, minute = 0, second = 1)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe estar en un horario válido'))'''

    # malicia
    def test_Reservacion_CamposVacios(self):
        form_data = {'inicio':datetime(year = 2000, month = 6, day = 15, hour = 6,  minute = 0), 'final':datetime(year = 2000, month = 6, day = 15, hour = 12,  minute = 0)}
        form = EstacionamientoReserva(data = form_data)
        self.assertEqual(form.is_valid(), True)
        
    '''def test_Reservacion_MasDeUnDia_NoPermitido(self):
        ReservaInicio = datetime(year=2000,month=2,day=6,hour = 11, minute = 59, second = 59)
        ReservaFin = datetime(year=2000,month=2,day=6,hour = 15, minute = 0, second = 1)
        HoraApertura = time(hour = 12, minute = 0, second = 0)
        HoraCierre = time(hour = 18, minute = 0, second = 0)
        x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
        self.assertEqual(x, (False, 'El horario de inicio de reserva debe estar en un horario válido'))'''

###############################################################################
# Marzullo
###############################################################################

class TestMarzullo(unittest.TestCase):
    '''
        Bordes:   7
        Esquinas: 6
        Malicia:  5

        Es importante definir el dominio de los datos que recibe Marzullo:

          cap. del est. +----------------------+
                        |                      |
                        |                      |
                        |                      |
                /\      |                      |
        cant. vehiculos |                      |
                \/      |                      |
                        |                      |
                        |                      |
                        |                      |
                      0 +----------------------+
                        |       <reserva>      |
                        |                      hora de cierre
                        |
                        hora de apertura

        Para los casos de prueba, manejamos un estacionamiento con apertura
        a las 6am y cierre a las 6pm, con capacidades que varían en cada caso.
        De esta forma, el dominio se vuelve:

          cap. del est. +--+--+--+--+--+--+--+--+--+--+--+--+
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                /\      |  |  |  |  |  |  |  |  |  |  |  |  |
        cant. vehiculos |  |  |  |  |  |  |  |  |  |  |  |  |
                \/      |  |  |  |  |  |  |  |  |  |  |  |  |
                        |  |  |  |  |zz|zz|zz|zz|zz|zz|  |  |
                        |  |  |  |yy|yy|yy|yy|  |  |  |  |  |
                        |xx|xx|xx|xx|xx|  |  |  |  |  |  |  |
                      0 +--+--+--+--+--+--+--+--+--+--+--+--+
                        |  |  |  |  |  |  |  |  |  |  |  |  |
                        06 07 08 09 10 11 12 13 14 15 16 17 18

        Donde las series de xs, ys y zs representan tres reservaciones,
        X, Y y Z, que van, respectivamente, de 6am a 11am, de 9am a 1pm, y de
        10am a 4pm. Podemos ver que la reservación X constituye un caso borde
        para Marzullo, puesto que su inicio coincide exactamente con la hora en
        la que abre el estacionamiento. Si decimos además que la capacidad
        del estacionamiento es 3, este caso se convierte en una esquina, puesto
        que el borde count=capacidad se alcanza entre las horas 10am y 11am.
    '''
    def crearEstacionamiento(self, puestos):
        e = Estacionamiento(
            propietario = "prop",
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            nroPuesto = puestos,
            apertura       = "06:00",
            reservasInicio = "06:00",
            cierre         = "18:00",
            reservasCierre = "18:00"
        )
        e.save()
        return e

    def testOneReservationMax(self): #borde, ocupación = capacidad
        e = self.crearEstacionamiento(1)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testOneReservationEarly(self): #borde, inicio = aprtura
        e = self.crearEstacionamiento(2)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,10)))

    def testOneReservationLate(self): #borde, fin = cierre
        e = self.crearEstacionamiento(2)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,15), datetime(2015,1,20,18)))

    def testOneReservationFullDay(self): #esquina, inicio = aprtura y fin = cierre
        e = self.crearEstacionamiento(1)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,18)))

    def testSmallestReservation(self): #borde, fin - inicio = 1hora
        e = self.crearEstacionamiento(1)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,8), datetime(2015,1,20,9)))

    def testAllSmallestReservations(self): #malicia, fin - inicio = 1hora, doce veces
        e = self.crearEstacionamiento(1)
        for i in range(12):
            Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 6+i), finalReserva = datetime(2015, 1, 20, 7+i)).save()
        for i in range(12):
            self.assertFalse(marzullo(e.id, datetime(2015,1,20,6+i), datetime(2015,1,20,7+i)))

    def testFullPlusOne(self): #malicia, fin - inicio = 1hora, doce veces + una reserva FullDay
        e = self.crearEstacionamiento(1)
        for i in range(12):
            Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 6+i), finalReserva = datetime(2015, 1, 20, 7+i)).save()
        self.assertFalse(marzullo(e.id, datetime(2015, 1, 20, 6), datetime(2015, 1, 20, 18)))

    def testNoSpotParking(self): #borde, capacidad = 0
        e = self.crearEstacionamiento(0)
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testTenSpotsOneReservation(self): #malicia
        e = self.crearEstacionamiento(10)
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testAddTwoReservation(self): #esquina, dos reservaciones con fin = cierre estac.
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva = datetime(2015, 1, 20, 9), finalReserva = datetime(2015, 1, 20, 18)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,12), datetime(2015,1,20,18)))

    def testAddTwoReservation2(self): #esquina, dos reservaciones con incio = apertura estac.
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,14)))

    def testAddThreeReservations(self): #malicia, reserva cubre todo el horario, y ocupación = capacidad
        e = self.crearEstacionamiento(3)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,18)))

    def testFiveSpotsFiveReservation(self): #borde, ocupación = capacidad
        e = self.crearEstacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,10), datetime(2015,1,20,18)))

    def testFiveSpotsSixReservation(self): #borde, ocupacion = capacidad antes de intentar hacer reservas nuevas
        e = self.crearEstacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,18)))
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,15)))

    def testFiveSpotsSixReservationNoOverlapping(self): #Dos esquinas, 1. count = capacidad, inicio=apertura
                                                        #              2. count = capacidad, fin=cierre
        e = self.crearEstacionamiento(5)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 12), finalReserva=datetime(2015, 1, 20, 17)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 17)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,6), datetime(2015,1,20,10)))
        #La reserva de arriba NO se concreta, puesto que sólo se verificó si era válida, sin agregar su objeto
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,18)))
        #De todos modos, la segunda falla, porque count = capacidad+1 a partir de las 12m

    def testManyReservationsMaxOverlapping(self): #esquina, count = capacidad en una hora (10am - 11am), algunas reservas tienen inicio = apertura
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  7), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  8), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  7), finalReserva=datetime(2015, 1, 20, 11)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  8), finalReserva=datetime(2015, 1, 20, 12)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  9), finalReserva=datetime(2015, 1, 20, 13)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20,  9)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20,  6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 10), finalReserva=datetime(2015, 1, 20, 15)).save()
        self.assertTrue(marzullo(e.id, datetime(2015,1,20,10), datetime(2015,1,20,15)))

    def testManyReservationsOneOverlap(self): #malicia, count = (capacidad+1) en la hora (9am - 10am), algunas reservas tienen inicio = apertura
        e = self.crearEstacionamiento(10)
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 7), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 8), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 9), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 7), finalReserva=datetime(2015, 1, 20, 11)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 8), finalReserva=datetime(2015, 1, 20, 12)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 9), finalReserva=datetime(2015, 1, 20, 13)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20,  9)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        Reserva(estacionamiento = e, inicioReserva=datetime(2015, 1, 20, 6), finalReserva=datetime(2015, 1, 20, 10)).save()
        self.assertFalse(marzullo(e.id, datetime(2015,1,20,9), datetime(2015,1,20,10)))

class RateTestCase(TestCase):

    #Pruebas para tarifa de hora y fraccion

    def test_oneHourFraccionPay(self):
        initial_time = datetime(2015,2,18,13,0)
        final_time = datetime(2015,2,18,14,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)

    def test_twoHourFraccionPay(self):
        initial_time = datetime(2015,2,18,13,0)
        final_time = datetime(2015,2,18,15,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),4)

    def test_halfHourFraccionPay(self):
        initial_time = datetime(2015,2,18,13,15)
        final_time = datetime(2015,2,18,13,45)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)

    def test_onePlusHalfHourFraccionPay(self):
        initial_time = datetime(2015,2,18,13,0)
        final_time = datetime(2015,2,18,14,30)
        rate = TarifaHorayFraccion(tarifa = 20)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),30)

    def test_DecimalFraccionPay(self):
        initial_time = datetime(2015,2,18,19,0)
        final_time = datetime(2015,2,18,20,15)
        rate = TarifaHorayFraccion(tarifa = 1)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1.5)

    def test_onePlusHalfPlusMinuteHourFraccionPay(self):
        initial_time = datetime(2015,2,18,15,15)
        final_time = datetime(2015,2,18,16,46)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),4)

    def test_oneDayMinusAMinuteFraccionPay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,18,23,59)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),48)
        
    def test_oneDayFractionPay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),48)
    
    def test_oneDayPlusAMinuteFractionPay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,1)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49) 
        
    def test_oneDayPlusHalfAnHourFractionPay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,30)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)
    
    def test_oneDayPlusThirtyOneMinutes(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,31)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),50)
        
    def testOneDayBeforeMidnightPlusAMinute(self):
        initial_time = datetime(2015,2,18,23,59)
        final_time = datetime(2015,2,20,0,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)
        
    def testOneDayThirtyMinutesBeforeMidnight_PusThirtyMinutes(self):
        initial_time = datetime(2015,2,18,23,30)
        final_time = datetime(2015,2,20,0,0)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),49)
    
    def testOneDayThirtyMinutesBeforeMidnight_PusThirtyOneMinutes(self):
        initial_time = datetime(2015,2,18,23,30)
        final_time = datetime(2015,2,20,0,1)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),50)
        
    def testTwoDays(self):
        initial_time = datetime(2015,2,18,6,30)
        final_time = datetime(2015,2,20,6,30)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),96)
    
    def testTwoDaysPlusOneMinute(self):
        initial_time = datetime(2015,2,18,6,30)
        final_time = datetime(2015,2,20,6,31)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),97)    
        
    def testSevenDays(self):
        initial_time = datetime(2015,2,18,6,30)
        final_time = datetime(2015,2,25,6,30)
        rate = TarifaHorayFraccion(tarifa = 2)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),7*24*2) 

    # Pruebas para la tarifa por minuto

    def test_oneMinutePay(self):
        initial_time = datetime(2015,2,18,15,1)
        final_time = datetime(2015,2,18,15,2)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1)

    def test_twoMinutePay(self):
        initial_time = datetime(2015,2,18,15,1)
        final_time = datetime(2015,2,18,15,3)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),2)
        
    def test_oneHourMinutePay(self):
        initial_time = datetime(2015,2,18,15,0)
        final_time = datetime(2015,2,18,16,0)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),60)


    def test_oneDayMinusOneMinuteMinutePay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,18,23,59)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1439)
        
    def test_oneDayMinutePay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,0)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1440)

    def test_oneDayPlusOneMinutePay(self):
        initial_time = datetime(2015,2,18,0,0)
        final_time = datetime(2015,2,19,0,1)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1441)
        
    def test_oneDayBeforeMidnightPlusOneMinute(self):
        initial_time = datetime(2015,2,18,23,59)
        final_time = datetime(2015,2,20,0,0)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),1441)
        
    def test_sevenDays(self):
        initial_time = datetime(2015,2,18,23,59)
        final_time = datetime(2015,2,25,23,59)
        rate = TarifaMinuto(tarifa = 60)
        self.assertEqual(rate.calcularPrecio(initial_time,final_time),7*24*60)
    
    # Pruebas para la clase tarifa	

    def test_OneHourRate(self):
        rate = TarifaHora(tarifa = 800)
        initial_datetime = datetime(2015,2,18,13,0)
        final_datetime = datetime(2015,2,18,14,0)
        value = rate.calcularPrecio(initial_datetime, final_datetime)
        self.assertEquals(value, 800)

    def test_MoreThanHourRate(self):
        rate = TarifaHora(tarifa = 800)
        initial_datetime = datetime(2015,2,18,6,8)
        final_datetime = datetime(2015,2,18,7,9)
        value = rate.calcularPrecio(initial_datetime, final_datetime)
        self.assertEquals(value, 1600)

    def test_LessThanAnHour(self):
        rate = TarifaHora(tarifa = 800)
        initial_datetime = datetime(2015,2,18,11,0)
        final_datetime = datetime(2015,2,18,11,15)
        value = rate.calcularPrecio(initial_datetime, final_datetime)
        self.assertEquals(value, 800)

    def testCompleteDayMinusOneMinute(self):
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,18,23,59)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 24)
        
    def testCompleteDay(self):
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,19,0,0)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 24)
        
    def testCompleteDayPlusOneMinute(self):
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,19,0,1)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 25)
        
    def testSevenDaysHourRate(self):
        rate=TarifaHora(tarifa=1)
        initial_time=datetime(2015,2,18,0,0)
        final_time=datetime(2015,2,25,0,0)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, 24*7)
        
    # Casos de decimales
    
    def testDecimalHourRate(self):
        rate=TarifaHora(tarifa=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,0)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, Decimal('0.9'))
    
    def testDecimalMinuteRate(self):
        rate=TarifaMinuto(tarifa=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,30)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, Decimal('1.05'))
        
    def testDecimalHourAndFractionRate(self):
        rate=TarifaHorayFraccion(tarifa=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,17,25)
        value = rate.calcularPrecio(initial_time, final_time)
        self.assertEqual(value, Decimal('0.75'))
