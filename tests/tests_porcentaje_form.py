# -*- coding: utf-8 -*-

from django.test import TestCase

from estacionamientos.forms import PorcentajeForm

###################################################################
#                    PORCENTAJE FORM
###################################################################

class PorcentajeFormTestCase(TestCase):

	#Borde
	def test_0(self):
	    form_data = {'porcentaje': '0.0'}
	    form = PorcentajeForm(data = form_data)
	    self.assertTrue(form.is_valid())

    #Borde
	def test_9(self):
	    form_data = {'porcentaje': '9.9'}
	    form = PorcentajeForm(data = form_data)
	    self.assertTrue(form.is_valid())

    #TDD
	def test_sin_decimales(self):
	    form_data = {'porcentaje': '1'}
	    form = PorcentajeForm(data = form_data)
	    self.assertFalse(form.is_valid())

    #TDD
	def test_mas_de_9(self):
	    form_data = {'porcentaje': '10.0'}
	    form = PorcentajeForm(data = form_data)
	    self.assertFalse(form.is_valid())

    #Borde
	def test_0_sin_decimales(self):
	    form_data = {'porcentaje': '0'}
	    form = PorcentajeForm(data = form_data)
	    self.assertFalse(form.is_valid())

    #Malicia
	def test_letras(self):
	    form_data = {'porcentaje': 'A'}
	    form = PorcentajeForm(data = form_data)
	    self.assertFalse(form.is_valid())

    #Malicia
	def test_vacio(self):
	    form_data = {}
	    form = PorcentajeForm(data = form_data)
	    self.assertFalse(form.is_valid())

    #TDD
	def test_3_decimales(self):
	    form_data = {'porcentaje': '1.234'}
	    form = PorcentajeForm(data = form_data)
	    self.assertFalse(form.is_valid())