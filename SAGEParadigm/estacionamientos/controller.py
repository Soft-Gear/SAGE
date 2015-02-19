# Archivo con funciones de control para SAGE
from estacionamientos.models import Estacionamiento
from datetime import date, datetime, timedelta, time

# chequeo de horarios de extended
def HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin):

	if HoraInicio >= HoraFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de inicio de reserva debe ser menor al horario de cierre')
	if ReservaInicio < HoraInicio:
		return (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertura del estacionamiento')
	if ReservaInicio > HoraFin:
		return (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento')
	if ReservaFin < HoraInicio:
		return (False, 'El horario de apertura de estacionamiento debe ser menor al horario de finalización de reservas')
	if ReservaFin > HoraFin:
		return (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas')
	return (True, '')

def validarHorarioReserva(ReservaInicio, ReservaFin, HorarioApertura, HorarioCierre):
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaFin - ReservaInicio < timedelta(hours=1):
			return (False, 'El tiempo de reserva debe ser al menos de 1 hora')
	if ReservaInicio < datetime.now():
		return (False, 'La reserva no puede tener lugar en el pasado.')
	if ReservaFin > datetime.now()+timedelta(days=7):
		return (False, 'La reserva no puede ser por mas de 7 dias')
	if HorarioApertura.hour==0 and HorarioApertura.minute==0 \
		and HorarioCierre.hour==23 and HorarioCierre.minute==59:
		seven_days=timedelta(days=7)
		if ReservaFin-ReservaInicio<=seven_days :
			return (True,'')
		else:
			return(False,'Se puede reservar un puesto por un maximo de 7 dias')
	else:
		delta=timedelta(hours=HorarioCierre.hour,minutes=HorarioCierre.minute)
		delta=delta-timedelta(hours=HorarioApertura.hour,minutes=HorarioApertura.minute)
		
		if ReservaFin-ReservaInicio>delta:
			return (False, 'El horario de inicio de reserva debe estar en un horario válido')
		else:
			hora_inicio=time(hour = ReservaInicio.hour, minute = ReservaInicio.minute)
			hora_final=time(hour = ReservaFin.hour, minute = ReservaFin.minute)
			if hora_inicio<HorarioApertura:
				return (False, 'El horario de inicio de reserva debe estar en un horario válido')
			if hora_final > HorarioCierre:
				return (False, 'El horario de cierre de reserva debe estar en un horario válido')
		return (True,'')

def marzullo(idEstacionamiento, hIn, hOut):
	e = Estacionamiento.objects.get(id = idEstacionamiento)
	ocupacion = []
	capacidad = e.nroPuesto

	for reserva in e.reserva_set.all():
		ocupacion += [(reserva.inicioReserva, 1), (reserva.finalReserva, -1)]
	ocupacion += [(hIn, 1), (hOut, -1)]

	count = 0
	for r in sorted(ocupacion):
		count += r[1]
		if count > capacidad:
			return False
	return True
