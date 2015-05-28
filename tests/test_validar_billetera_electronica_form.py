# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import ValidarBilleteraForm

###################################################################
#                    VALIDAR BILLETERA FORM
###################################################################

class ValidarBilleteraElectronicaFormTestCase(TestCase):

    #caso malicia
    def test_campos_vacios(self):
        form_data = {}
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_solo_un_campo_necesario(self):
        form_data = {
            'idValid': '12345678'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_todos_los_campos_necesarios(self):
        form_data = {
            'idValid': '12345678',
            'pinValid': '0000'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #malicia
    def test_id_caracteres_invalidos(self):
        form_data = {
            'idValid': '12345678&&!!678',
            'pinValid': '0000'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #malicia
    def test_id_letras_en_el_campo(self):
        form_data = {
            'idValid': '1234567ghy678',
            'pinValid': '0000'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    #borde    
    def test_id_minimo(self):
        form_data = {
            'idValid': '1',
            'pinValid': '0000'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #malicia
    def test_pin_caracteres_invalidos(self):
        form_data = {
            'idValid': '1234567',
            'pinValid': '00(&'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid()) 
        
    #malicia
    def test_pin_letras_en_el_campo(self):
        form_data = {
            'idValid': '12345667',
            'pinValid': '00ab'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #malicia
    def test_pin_muy_grande(self):
        form_data = {
            'idValid': '12345667',
            'pinValid': '00000'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    def test_pin_muy_pequeno(self):
        form_data = {
            'idValid': '12345667',
            'pinValid': '000'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    