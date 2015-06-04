# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import BilleteraElectronicaForm, ValidarBilleteraForm, RecargarSaldoForm

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
            'nombreUsu': 'Juan'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_dos_campos_necesarios(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_tres_campos_necesarios(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())

    # caso borde
    def test_todos_los_campos_necesarios(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
    
    # caso borde
    def test_nombre_pequeno(self):
        form_data = {
            'nombreUsu': 'J',
            'ciUsu': 'V-12345678',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())    
        
    # malicia
    def test_nombre_invalido_digitos_en_campo(self):
        form_data = {
            'nombreUsu': 'Juan1234',
            'ciUsu': 'V-12345678',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_nombre_invalido_simbolos_especiales(self):
        form_data = {
            'nombreUsu': 'J#u$a%n!',
            'ciUsu': 'V-123456789',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # caso borde
    def test_CI_tamano_invalido(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-1234',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # caso borde
    def test_CI_minima(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-100000',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # malicia
    def test_CI_formato_invalido(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'Dani123456789',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    def test_CI_invalida_simbolos_especiales(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V~12345678',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
    
    # malicia
    def test_CI_invalida_simbolos_especiales2(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V- 12345678',
            'pinUsu': '1234'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    '''def test_idBilletera_invalido_simbolos_especiales(self):
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
        self.assertTrue(form.is_valid())'''
        
    # caso borde
    def test_PIN_minimo(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': '0000'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertTrue(form.is_valid())
    
    # malicia
    def test_PIN_invalido_simbolos_especiales(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': '1\'!0'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_PIN_invalido_simbolos_especiales2(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': '1#34'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # malicia
    def test_PIN_invalido_letras_en_campo(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': 'ab3d'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_PIN_corto_invalido(self):
        form_data = {
            'nombreUsu': 'Juan',
            'ciUsu': 'V-12345678',
            'pinUsu': '123'
        }
        form = BilleteraElectronicaForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #caso malicia
    def test_campos_vacios_validar(self):
        form_data = {}
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_solo_un_campo_necesario_validar(self):
        form_data = {
            'idValid': '12345678'
        }
        form = ValidarBilleteraForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # caso borde
    def test_todos_los_campos_necesarios_validar(self):
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
            'idValid': '123456678',
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
        
    def test_RecargarBilletera_vacio(self):
        form_data = {}
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_unCampo(self):
        form_data = {
            'nombre': 'Pedro1'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_dosCampos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_tresCampos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedula': '123456789'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_cuatroCampos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_cincoCampos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_seisCampos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_sieteCampos(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_completo(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'500'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #malicia
    def test_RecargarBilletera_caracteres_en_ID(self):
        form_data = {
            'nombre': 'Pedro1',
            'apellido': 'Perez',
            'cedula': '123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0fhfdhgfg',
            'pinValid':'0000',
            'monto':'500'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_pinTresDigitos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'000',
            'monto':'500'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
     #borde
    def test_RecargarBilletera_pinCincoDigitos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'00000',
            'monto':'500'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
        
    #malicia
    def test_RecargarBilletera_pin_con_caracteres(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'00j0',
            'monto':'500'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoCuatroDigitos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'1000'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoCincoDigitos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'10000'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoUnDecimal(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'100.1'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoDosDecimales(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'100.11'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #malicia
    def test_RecargarBilletera_montoSinDecimales(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'100.'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoMinimo(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'0.01'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoInvalido(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'0.00'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    #borde
    def test_RecargarBilletera_montoInvalidoDos(self):
        form_data = {
            'nombre': 'Pedro',
            'apellido': 'Perez',
            'cedula': 'V-123456789',
            'tarjetaTipo': 'Vista',
            'tarjeta': '1234567890123456',
            'idBill' : '0',
            'pinValid':'0000',
            'monto':'2.0'
        }
        form = RecargarSaldoForm(data = form_data)
        self.assertFalse(form.is_valid())

    
