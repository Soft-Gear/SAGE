# -*- coding: utf-8 -*-
from django.db import models
from math import ceil, floor
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from decimal import Decimal
from datetime import timedelta

class Propietario(models.Model):
	nombre   = models.CharField(max_length = 30)
	apellido = models.CharField(max_length = 30)
	ci       = models.CharField(max_length = 12, unique = True)
	tel      = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre + " " + self.apellido

class Estacionamiento(models.Model):
	ci_propietario = models.ForeignKey(Propietario) #CI del propietario! No el nombre.
	nombre      = models.CharField(max_length = 50)
	direccion   = models.TextField(max_length = 120)
	telefono1   = models.CharField(blank = True, null = True, max_length = 30)
	telefono2   = models.CharField(blank = True, null = True, max_length = 30)
	telefono3   = models.CharField(blank = True, null = True, max_length = 30)
	email1      = models.EmailField(blank = True, null = True)
	email2      = models.EmailField(blank = True, null = True)
	rif         = models.CharField(max_length = 12)

	# Campos para referenciar al esquema de tarifa

	content_type = models.ForeignKey(ContentType, null = True)
	object_id    = models.PositiveIntegerField(null = True)
	tarifa       = GenericForeignKey()
	apertura     = models.TimeField(blank = True, null = True)
	cierre       = models.TimeField(blank = True, null = True)
	capacidad    = models.IntegerField(blank = True, null = True)

	def __str__(self):
		return self.nombre+' '+str(self.ci_propietario)

class Reserva(models.Model):
	nombre 			= models.CharField(max_length = 30)
	apellido        = models.CharField(max_length = 30)
	ci				= models.CharField(max_length = 12)
	estacionamiento = models.ForeignKey(Estacionamiento)
	inicioReserva   = models.DateTimeField()
	finalReserva    = models.DateTimeField()

	def __str__(self):
		return self.estacionamiento.nombre+' ('+str(self.inicioReserva)+','+str(self.finalReserva)+')'
	
class ConfiguracionSMS(models.Model):
	estacionamiento = models.ForeignKey(Estacionamiento)
	inicioReserva   = models.DateTimeField()
	finalReserva    = models.DateTimeField()

	def __str__(self):
		return self.estacionamiento.nombre+' ('+str(self.inicioReserva)+','+str(self.finalReserva)+')'

class Pago(models.Model):
	fechaTransaccion = models.DateTimeField()
	cedula           = models.CharField(max_length = 10)
	tipoPago         = models.CharField(max_length = 30)
	reserva          = models.ForeignKey(Reserva)
	monto            = models.DecimalField(decimal_places = 2, max_digits = 256)
	estado           = models.BooleanField(default = True)

	def __str__(self):
		return str(self.id)+" "+str(self.reserva.estacionamiento.nombre)+" "+str(self.cedulaTipo)+"-"+str(self.cedula)
		
class Factura_devolucion(models.Model):
	fechaTransaccion     = models.DateTimeField()
	numReciboPago        = models.IntegerField()
	idBilleteraRecargada = models.IntegerField()
	monto                = models.DecimalField(decimal_places = 2, max_digits = 256)
	estado               = models.BooleanField(default = True)
		
class BilleteraElectronica(models.Model):
	idBilletera = models.IntegerField()
	PIN         = models.CharField(max_length = 4)
	nombre      = models.CharField(max_length = 30)
	apellido    = models.CharField(max_length = 30)
	CI          = models.CharField(max_length = 10)
	saldo       = models.DecimalField(decimal_places= 2, max_digits = 256)
	
	def __str__(self):
		return self.nombre + " " + self.idBilletera + " " + str(self.id)    

class HistorialBilleteraElectronica(models.Model):
	billetera		 = models.ForeignKey(BilleteraElectronica)
	fechaTransaccion = models.DateTimeField()
	tipo			 = models.CharField(max_length = 10)
	nombre		     = models.CharField(max_length = 30)
	apellido         = models.CharField(max_length = 30)
	cedula           = models.CharField(max_length = 10)
	tarjeta			 = models.CharField(blank = True, max_length = 16, default = "")
	debito 			 = models.DecimalField(decimal_places= 2, max_digits = 256, blank = True, null = True)
	credito			 = models.DecimalField(decimal_places= 2, max_digits = 256, blank = True, null = True)
	
	def __str__(self):
		return str(self.billetera.idBilletera) + " " + str(self.fechaTransaccion) + " " + self.tipo + " " + self.nombre
	
class EsquemaTarifario(models.Model):

	# No se cuantos digitos deberiamos poner
	tarifa         = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa2        = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	inicioEspecial = models.TimeField(blank = True, null = True)
	finEspecial    = models.TimeField(blank = True, null = True)

	class Meta:
		abstract = True
	def __str__(self):
		return str(self.tarifa)


class TarifaHora(EsquemaTarifario):
	def calcularPrecio(self,horaInicio,horaFinal):
		a = horaFinal-horaInicio
		a = a.days*24+a.seconds/3600
		a = ceil(a) #  De las horas se calcula el techo de ellas
		return(Decimal(self.tarifa*a).quantize(Decimal('1.00')))
	def tipo(self):
		return("Por Hora")

class TarifaMinuto(EsquemaTarifario):
	def calcularPrecio(self,horaInicio,horaFinal):
		minutes = horaFinal-horaInicio
		minutes = minutes.days*24*60+minutes.seconds/60
		return (Decimal(minutes)*Decimal(self.tarifa/60)).quantize(Decimal('1.00'))
	def tipo(self):
		return("Por Minuto")

class TarifaHorayFraccion(EsquemaTarifario):
	def calcularPrecio(self,horaInicio,horaFinal):
		time = horaFinal-horaInicio
		time = time.days*24*3600+time.seconds
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
		return(Decimal(valor).quantize(Decimal('1.00')))

	def tipo(self):
		return("Por Hora y Fraccion")

class TarifaFinDeSemana(EsquemaTarifario):
	def calcularPrecio(self,inicio,final):
		minutosNormales    = 0
		minutosFinDeSemana = 0
		tiempoActual       = inicio
		minuto             = timedelta(minutes=1)
		while tiempoActual < final:
			# weekday() devuelve un numero del 0 al 6 tal que
			# 0 = Lunes
			# 1 = Martes
			# ..
			# 5 = Sabado
			# 6 = Domingo
			if tiempoActual.weekday() < 5:
				minutosNormales += 1
			else:
				minutosFinDeSemana += 1
			tiempoActual += minuto
		return Decimal(
			minutosNormales*self.tarifa/60 +
			minutosFinDeSemana*self.tarifa2/60
		).quantize(Decimal('1.00'))

	def tipo(self):
		return("Tarifa diferenciada para fines de semana")

class TarifaHoraPico(EsquemaTarifario):
	def calcularPrecio(self,reservaInicio,reservaFinal):
		minutosPico  = 0
		minutosValle = 0
		tiempoActual = reservaInicio
		minuto       = timedelta(minutes=1)
		while tiempoActual < reservaFinal:
			horaActual = tiempoActual.time()
			if horaActual >= self.inicioEspecial and horaActual < self.finEspecial:
				minutosPico += 1
			elif horaActual < self.inicioEspecial or horaActual >= self.finEspecial:
				minutosValle += 1
			tiempoActual += minuto
		return Decimal(
			minutosPico*self.tarifa2/60 +
			minutosValle*self.tarifa/60
		).quantize(Decimal('1.00'))

	def tipo(self):
		return("Tarifa diferenciada por hora pico")
