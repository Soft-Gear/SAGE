# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import PropietarioForm

###################################################################
#                    PROPIETARIO_ALL FORM
###################################################################

class PropietarioAllFormTestCase(TestCase):

    # malicia
    def test_campos_vacios(self):
        form_data = {}
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_solo_un_campo_necesario(self):
        form_data = {
            'nombreProp': 'Pedro'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_dos_campos_necesarios(self):
        form_data = {
            'nombreProp': 'Pedro',
            'ci': 'V-12345678'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_todos_los_campos_necesarios(self):
        form_data = {
            'nombreProp': 'Pedro',
            'ci': 'V-12345678',
            'telefono': '02129322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    # caso borde
    def test_nombre_valido_dieresis_acento(self):
        form_data = {
            'nombreProp': 'María Güilo',
            'ci': 'V-12345678',
            'telefono': '02129322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    # caso borde
    def test_nombre_valido_guion_comilla(self):
        form_data = {
            'nombreProp': 'D\'Angostino-FebresÑu',
            'ci': 'V-12345678',
            'telefono': '02129322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_nombre_invalido_digitos_en_campo(self):
        form_data = {
            'nombreProp': 'Pedro132',
            'ci': 'V-12345678',
            'telefono': '02129322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_nombre_invalido_simbolos_especiales(self):
        form_data = {
            'nombreProp': 'Pedro!',
            'ci': 'V-12345678',
            'telefono': '02129322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_CI_formato_invalido(self):
        form_data = {
            'nombreProp': 'Pedro132',
            'ci': 'Kaa123456789',
            'telefono': '02129322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_formato_invalido_telefono(self):
        form_data = {
            'nombreProp': 'Pedro',
            'ci': 'V-12345678',
            'telefono': '02193228782'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_tamano_invalido_telefono(self):
        form_data = {
            'nombreProp': 'Pedro',
            'ci': 'V-12345678',
            'telefono_1': '0212322878'
        }
        form = PropietarioForm(data = form_data)
        self.assertFalse(form.is_valid())