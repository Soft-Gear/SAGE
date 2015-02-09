# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm


class Estacionamiento(models.Model):
	propietario = models.CharField(max_length = 50, help_text = "Nombre Propio")
	nombre = models.CharField(max_length = 50)
	direccion = models.TextField(max_length = 120)

	telefono1 = models.CharField(blank = True, null = True, max_length = 30)
	telefono2 = models.CharField(blank = True, null = True, max_length = 30)
	telefono3 = models.CharField(blank = True, null = True, max_length = 30)

	email1 = models.EmailField(blank = True, null = True)
	email2 = models.EmailField(blank = True, null = True)

	rif = models.CharField(max_length = 12)

	tarifa = models.CharField(max_length = 50, blank = True, null = True)
	apertura = models.TimeField(blank = True, null = True)
	cierre = models.TimeField(blank = True, null = True)
	reservasInicio = models.TimeField(blank = True, null = True)
	reservasCierre = models.TimeField(blank = True, null = True)
	nroPuesto = models.IntegerField(blank = True, null = True)

class ReservasModel(models.Model):
	estacionamiento = models.ForeignKey(Estacionamiento)
	inicioReserva = models.TimeField()
	finalReserva = models.TimeField()
