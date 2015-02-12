# -*- coding: utf-8 -*-
from django.db import models
from math import ceil, floor
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import time, timedelta
from math import ceil

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

	# Campos para referenciar al esquema de tarifa

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	esquemaTarifa = GenericForeignKey()


	tarifa = models.CharField(max_length = 50, blank = True, null = True)
	apertura = models.TimeField(blank = True, null = True)
	cierre = models.TimeField(blank = True, null = True)
	reservasInicio = models.TimeField(blank = True, null = True)
	reservasCierre = models.TimeField(blank = True, null = True)
	nroPuesto = models.IntegerField(blank = True, null = True)


class Reserva(models.Model):
	estacionamiento = models.ForeignKey(Estacionamiento)
	inicioReserva = models.TimeField()
	finalReserva = models.TimeField()

class EsquemaTarifario(models.Model):
	# No se cuantos digitos o decimales deberiamos poner
	tarifa = models.DecimalField(max_digits=10, decimal_places=4) 

	class Meta:
		abstract = True


class TarifaHora(EsquemaTarifario):

	def calcularPrecio(self,horaInicio,horaFinal):
		time = (horaFinal-horaInicio).seconds+((horaFinal-horaInicio).days)*86400
		a=ceil(time/3600) #  De los segundos se calculan las horas en la funcion techo
		return(self.tarifa*a)

class TarifaMinuto(EsquemaTarifario):

	def calcularPrecio(self,horaInicio,horaFinal):
		if(horaInicio>=horaFinal):
			raise ValueError("Fechas inválidos.")
		time = (horaFinal-horaInicio).seconds+((horaFinal-horaInicio).days)*86400
		print("---"+str(time)+"---")
		minutes = ceil(time/60)
		return (minutes*self.tarifa)
	
class TarifaHorayFraccion(EsquemaTarifario):

	def calcularPrecio(self,horaInicio,horaFinal):
		#en este modelo se supone que la tarifa es lo que cuesta una hora
		if(horaInicio>=horaFinal):
			raise ValueError("Fechas inválidos.")
		time = (horaFinal-horaInicio).seconds+((horaFinal-horaInicio).days)*86400
		if(time>3600):
			valor = (floor(time/3600)*self.tarifa)
			if((time%3600)==0):
				pass
			elif((time%3600)>1800):
				valor += self.tarifa
			else:
				valor += self.tarifa/2
		else:
			valor = self.tarifa
		return valor
