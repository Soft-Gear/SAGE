# -*- coding: utf-8 -*-
from django.db import models
from math import ceil, floor
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from decimal import Decimal
from datetime import timedelta

class Propietario(models.Model):
	nombre = models.CharField(max_length = 50)
	ci     = models.CharField(max_length = 12, unique = True)
	tel    = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre

class Estacionamiento(models.Model):
	ci_propietario = models.ForeignKey("Propietario") #CI del propietario! No el nombre.
	nombre      = models.CharField(max_length = 50)
	direccion   = models.TextField(max_length = 120)
	telefono1   = models.CharField(blank = True, null = True, max_length = 30)
	telefono2   = models.CharField(blank = True, null = True, max_length = 30)
	telefono3   = models.CharField(blank = True, null = True, max_length = 30)
	email1      = models.EmailField(blank = True, null = True)
	email2      = models.EmailField(blank = True, null = True)
	rif         = models.CharField(max_length = 12)

	# Campos para referenciar al esquema de tarifa

	content_type 			= models.ForeignKey(ContentType, null = True)
	object_id    			= models.PositiveIntegerField(null = True)
	tarifa       			= GenericForeignKey()
	apertura     			= models.TimeField(blank = True, null = True)
	cierre       			= models.TimeField(blank = True, null = True)
	capacidad_motos    		= models.IntegerField(blank = True, null = True)
	capacidad_carros    	= models.IntegerField(blank = True, null = True)
	capacidad_camiones  	= models.IntegerField(blank = True, null = True)
	capacidad_microbus  	= models.IntegerField(blank = True, null = True)
	capacidad_autobus   	= models.IntegerField(blank = True, null = True)
	capacidad_especiales    = models.IntegerField(blank = True, null = True)
	capacidad 			    = models.IntegerField(blank = True, null = True)



	def __str__(self):
		return self.nombre+' '+str(self.ci_propietario)

class Reserva(models.Model):
	estacionamiento = models.ForeignKey(Estacionamiento)
	inicioReserva   = models.DateTimeField()
	finalReserva    = models.DateTimeField()
	tipoVehiculo	= models.CharField(max_length = 10)

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
		
class Recarga_billetera(models.Model):
	fechaTransaccion = models.DateTimeField()
	idBilletera 	 = models.IntegerField()
	nombre		     = models.CharField(max_length = 30)
	apellido         = models.CharField(max_length = 30)
	cedula           = models.CharField(max_length = 10)
	monto            = models.DecimalField(decimal_places = 2, max_digits = 256)
	estado           = models.BooleanField(default = True)
	
	def __str__(self):
		return self.nombre + " " + self.idBilletera + " " + str(self.id)

class BilleteraElectronica(models.Model):
	idBilletera = models.IntegerField()
	PIN         = models.CharField(max_length = 4)
	nombre      = models.CharField(max_length = 50)
	CI          = models.CharField(max_length = 10)
	saldo       = models.DecimalField(decimal_places= 2, max_digits = 256)
	
	def __str__(self):
		return self.nombre + " " + self.idBilletera + " " + str(self.id)    

class EsquemaTarifario(models.Model):

	# No se cuantos digitos deberiamos poner
	tarifa_motos         = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa_carros        = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa_camiones      = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa_microbus      = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa_autobus       = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa_especiales    = models.DecimalField(max_digits=20, decimal_places=2)
	tarifa2_motos        = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	tarifa2_carros       = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	tarifa2_camiones     = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	tarifa2_microbus     = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	tarifa2_autobus      = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	tarifa2_especiales   = models.DecimalField(blank = True, null = True, max_digits=10, decimal_places=2)
	inicioEspecial 		 = models.TimeField(blank = True, null = True)
	finEspecial    		 = models.TimeField(blank = True, null = True)

	class Meta:
		abstract = True
	def __str__(self):
		return str(self.tarifa)


class TarifaHora(EsquemaTarifario):
	def calcularPrecio(self,horaInicio,horaFinal,tipoVehiculo):
		a = horaFinal-horaInicio
		a = a.days*24+a.seconds/3600
		a = ceil(a) #  De las horas se calcula el techo de ellas
		if tipoVehiculo == 'moto':
			return(Decimal(self.tarifa_motos*a).quantize(Decimal('1.00')))
		elif tipoVehiculo == 'carro':
			return(Decimal(self.tarifa_carros*a).quantize(Decimal('1.00')))
		elif tipoVehiculo == 'camion':
			return(Decimal(self.tarifa_camiones*a).quantize(Decimal('1.00')))
		elif tipoVehiculo == 'microbus':
			return(Decimal(self.tarifa_microbus*a).quantize(Decimal('1.00')))
		elif tipoVehiculo == 'autobus':
			return(Decimal(self.tarifa_autobus*a).quantize(Decimal('1.00')))
		elif tipoVehiculo == 'especial':
			return(Decimal(self.tarifa_especiales*a).quantize(Decimal('1.00')))
	def tipo(self):
		return("Por Hora")

class TarifaMinuto(EsquemaTarifario):
	def calcularPrecio(self,horaInicio,horaFinal,tipoVehiculo):
		minutes = horaFinal-horaInicio
		minutes = minutes.days*24*60+minutes.seconds/60
		if tipoVehiculo == 'moto':
			return (Decimal(minutes)*Decimal(self.tarifa_motos/60)).quantize(Decimal('1.00'))
		elif tipoVehiculo == 'carro':
			return (Decimal(minutes)*Decimal(self.tarifa_carros/60)).quantize(Decimal('1.00'))
		elif tipoVehiculo == 'camion':
			return (Decimal(minutes)*Decimal(self.tarifa_camiones/60)).quantize(Decimal('1.00'))
		elif tipoVehiculo == 'microbus':
			return (Decimal(minutes)*Decimal(self.tarifa_microbus/60)).quantize(Decimal('1.00'))
		elif tipoVehiculo == 'autobus':
			return (Decimal(minutes)*Decimal(self.tarifa_autobus/60)).quantize(Decimal('1.00'))
		elif tipoVehiculo == 'especial':
			return (Decimal(minutes)*Decimal(self.tarifa_especiales/60)).quantize(Decimal('1.00'))
	def tipo(self):
		return("Por Minuto")

class TarifaHorayFraccion(EsquemaTarifario):
	def calcularPrecio(self,horaInicio,horaFinal,tipoVehiculo):
		time = horaFinal-horaInicio
		time = time.days*24*3600+time.seconds
		#tarifa segun tipo de vehículo
		if tipoVehiculo == 'moto':
			tarifa = self.tarifa_motos
		elif tipoVehiculo == 'carro':
			tarifa = self.tarifa_carros
		elif tipoVehiculo == 'camion':
			tarifa = self.tarifa_camiones
		elif tipoVehiculo == 'microbus':
			tarifa = self.tarifa_microbus
		elif tipoVehiculo == 'autobus':
			tarifa = self.tarifa_autobus
		elif tipoVehiculo == 'especial':
			tarifa = self.tarifa_especiales

		if(time>3600):
			valor = (floor(time/3600)*tarifa)
			if((time%3600)==0):
				pass
			elif((time%3600)>1800):
				valor += tarifa
			else:
				valor += tarifa/2
		else:
			valor = tarifa
		return(Decimal(valor).quantize(Decimal('1.00')))

	def tipo(self):
		return("Por Hora y Fraccion")

class TarifaFinDeSemana(EsquemaTarifario):
	def calcularPrecio(self,inicio,final,tipoVehiculo):
		minutosNormales    = 0
		minutosFinDeSemana = 0
		tiempoActual       = inicio
		minuto             = timedelta(minutes=1)
		#tarifa segun tipo de vehículo
		if tipoVehiculo == 'moto':
			tarifa = self.tarifa_motos
			tarifa2 = self.tarifa2_motos
		elif tipoVehiculo == 'carro':
			tarifa = self.tarifa_carros
			tarifa2 = self.tarifa2_carros
		elif tipoVehiculo == 'camion':
			tarifa = self.tarifa_camiones
			tarifa2 = self.tarifa2_camiones
		elif tipoVehiculo == 'microbus':
			tarifa = self.tarifa_microbus
			tarifa2 = self.tarifa2_microbus
		elif tipoVehiculo == 'autobus':
			tarifa = self.tarifa_autobus
			tarifa2 = self.tarifa2_autobus
		elif tipoVehiculo == 'especial':
			tarifa = self.tarifa_especiales
			tarifa2 = self.tarifa2_especiales

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
			minutosNormales*tarifa/60 +
			minutosFinDeSemana*tarifa2/60
		).quantize(Decimal('1.00'))

	def tipo(self):
		return("Tarifa diferenciada para fines de semana")

class TarifaHoraPico(EsquemaTarifario):
	def calcularPrecio(self,reservaInicio,reservaFinal,tipoVehiculo):
		minutosPico  = 0
		minutosValle = 0
		tiempoActual = reservaInicio
		minuto       = timedelta(minutes=1)
		#tarifa segun tipo de vehículo
		if tipoVehiculo == 'moto':
			tarifa = self.tarifa_motos
			tarifa2 = self.tarifa2_motos
		elif tipoVehiculo == 'carro':
			tarifa = self.tarifa_carros
			tarifa2 = self.tarifa2_carros
		elif tipoVehiculo == 'camion':
			tarifa = self.tarifa_camiones
			tarifa2 = self.tarifa2_camiones
		elif tipoVehiculo == 'microbus':
			tarifa = self.tarifa_microbus
			tarifa2 = self.tarifa2_microbus
		elif tipoVehiculo == 'autobus':
			tarifa = self.tarifa_autobus
			tarifa2 = self.tarifa2_autobus
		elif tipoVehiculo == 'especial':
			tarifa = self.tarifa_especiales
			tarifa2 = self.tarifa2_especiales

		while tiempoActual < reservaFinal:
			horaActual = tiempoActual.time()
			if horaActual >= self.inicioEspecial and horaActual < self.finEspecial:
				minutosPico += 1
			elif horaActual < self.inicioEspecial or horaActual >= self.finEspecial:
				minutosValle += 1
			tiempoActual += minuto
		return Decimal(
			minutosPico*tarifa2/60 +
			minutosValle*tarifa/60
		).quantize(Decimal('1.00'))

	def tipo(self):
		return("Tarifa diferenciada por hora pico")
