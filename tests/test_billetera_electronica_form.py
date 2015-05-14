# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import BilleteraElectronicaForm

###################################################################
#                    BILLETERAELECTRONICA_ALL FORM
###################################################################

class BilleteraElectronicaAllFormTestCase(TestCase):

    # malicia
    def test_campos_vacios(self):
        form_data = {}
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_solo_un_campo_necesario(self):
        form_data = {
            'idBilletera': '12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_dos_campos_necesarios(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_tres_campos_necesarios(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_todos_los_campos_necesarios(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
    
    # caso borde
    def test_nombre_pequeno(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'A',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())    
        
    # malicia
    def test_nombre_invalido_digitos_en_campo(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan524',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_nombre_invalido_simbolos_especiales(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'J#u$a%n!',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # caso borde
    def test_CI_tamano_invalido(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-99999'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # caso borde
    def test_CI_minima(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-100000'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # malicia
    def test_CI_formato_invalido(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'Dani123456789'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    def test_CI_invalida_simbolos_especiales(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V~12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # malicia
    def test_CI_invalida_simbolos_especiales2(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V- 12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    def test_idBilletera_invalido_simbolos_especiales(self):
        form_data = {
            'idBilletera': '12345678910!"/(',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # malicia
    def test_idBilletera_invalido_simbolos_especiales2(self):
        form_data = {
            'idBilletera': '123456 78910',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    def test_idBilletera_invalido_letras_en_campo(self):
        form_data = {
            'idBilletera': '123456789abcHT',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # caso borde
    def test_idBilletera_minimo(self):
        form_data = {
            'idBilletera': '0',
            'PIN': '87654321',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # caso borde
    def test_PIN_minimo(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '0',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
    
    # malicia
    def test_PIN_invalido_simbolos_especiales(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '12345678910!"/(',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_PIN_invalido_simbolos_especiales2(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '123456 78910',
            'nombre': 'Juan',
            'CI': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    def test_PIN_invalido_letras_en_campo(self):
        form_data = {
            'idBilletera': '12345678',
            'PIN': '123456789abcHT',
            'nombre': 'Juan',
            'CI': 'V-123456789'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    

    
