# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import CancelarReservaForm

###################################################################
#                    CANCELAR_RESERVA_ALL FORM
###################################################################


class CancelarReservaAllTestCase(TestCase):


    # malicia
    def test_campos_vacios(self):
        form_data = {}
        form = CancelarReservaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_solo_un_campo_puesto(self):
        form_data = {
            'cedula': 'V-12345678'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_dos_campos_necesarios(self):
        form_data = {
            'cedula': 'V-12345678',
            'idReserva': '6'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # caso borde
    def test_longitud_cedula_minima_incorrecta(self):
        form_data = {
            'cedula': 'V-12345',
            'idReserva': '6'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_longitud_cedula_minima_correcta(self):
        form_data = {
            'cedula': 'V-123456',
            'idReserva': '6'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertTrue(form.is_valid())
     
    # caso borde
    def test_digitos_cedula_minima_incorrecta(self):
        form_data = {
            'cedula': 'V-00000000',
            'idReserva': '6'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertFalse(form.is_valid())
           
    # caso borde
    def test_digitos_cedula_minima_correcta(self):
        form_data = {
            'cedula': 'V-10000000',
            'idReserva': '6'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertTrue(form.is_valid())
    
    # caso borde
    def test_ideReserva_valor_grande_correcto(self):
        form_data = {
            'cedula': 'V-12345678',
            'idReserva': '9999999999999999999999999'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertTrue(form.is_valid())
           
    # caso borde
    def test_ideReserva_valor_minimo_correcto(self):
        form_data = {
            'cedula': 'V-12345678',
            'idReserva': '0'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # caso malicia
    def test_forma_minima_correcta(self):
        form_data = {
            'cedula': 'V-100000',
            'idReserva': '0'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #caso malicia
    def test_cedula_solo_nacionalidad(self):
        form_data = {
            'cedula': 'V-',
            'idReserva': '6'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #caso malicia
    def test_idReserva_caracter(self):
        form_data = {
            'cedula': 'V-12345678',
            'idReserva': 'H'
        }
        form = CancelarReservaForm(data = form_data)
        self.assertFalse(form.is_valid())