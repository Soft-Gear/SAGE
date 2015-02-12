# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from decimal import Decimal
from estacionamientos.controller import *
from estacionamientos.forms import EstacionamientoExtendedForm, EstacionamientoExtendedForm2
from estacionamientos.forms import EstacionamientoForm
from estacionamientos.forms import EstacionamientoReserva
from estacionamientos.forms import PagoTarjetaDeCredito
from estacionamientos.models import Estacionamiento, Reserva, TarifaHora, TarifaMinuto, TarifaHorayFraccion
reservaFinal = ""


# Usamos esta vista para procesar todos los estacionamientos
def estacionamientos_all(request):
    estacionamientos = Estacionamiento.objects.all()

    # Si es un GET, mandamos un formulario vacio
    if request.method == 'GET':

        form = EstacionamientoForm()

    # Si es POST, se verifica la información recibida
    elif request.method == 'POST':
        # Creamos un formulario con los datos que recibimos
        form = EstacionamientoForm(request.POST)

        # Parte de la entrega era limitar la cantidad maxima de
        # estacionamientos a 5
        if len(estacionamientos) >= 5:
            return render(request, 'templateMensaje.html',
                          {'color':'red', 'mensaje':'No se pueden agregar más estacionamientos'})

        # Si el formulario es valido, entonces creamos un objeto con
        # el constructor del modelo
        if form.is_valid():
            obj = Estacionamiento(
                propietario = form.cleaned_data['propietario'],
                nombre = form.cleaned_data['nombre'],
                direccion = form.cleaned_data['direccion'],
                rif = form.cleaned_data['rif'],
                telefono1 = form.cleaned_data['telefono_1'],
                telefono2 = form.cleaned_data['telefono_2'],
                telefono3 = form.cleaned_data['telefono_3'],
                email1 = form.cleaned_data['email_1'],
                email2 = form.cleaned_data['email_2']
            )
            obj.save()
            # Recargamos los estacionamientos ya que acabamos de agregar
            estacionamientos = Estacionamiento.objects.all()
            form = EstacionamientoForm()

    return render(request, 'base.html', {'form': form, 'estacionamientos': estacionamientos})

def estacionamiento_detail(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    if request.method == 'GET':

        form = EstacionamientoExtendedForm()
        form2 = EstacionamientoExtendedForm2()

    elif request.method == 'POST':
        # Leemos el formulario
        form = EstacionamientoExtendedForm(request.POST)
        form2 = EstacionamientoExtendedForm2(request.POST)
        # Si el formulario
        if form.is_valid() and form2.is_valid():
            horaIn = form.cleaned_data['horarioin']
            horaOut = form.cleaned_data['horarioout']
            reservaIn = form.cleaned_data['horario_reserin']
            reservaOut = form.cleaned_data['horario_reserout']
            tipo = form2.cleaned_data['esquema']
            tmonto = form.cleaned_data['tarifa']
            if(tipo=='Por hora'):
                t = TarifaHora(tarifa = tmonto)
            elif(tipo=='Por minuto'):
                t = TarifaMinuto(tarifa = tmonto)
            elif(tipo=='Por fraccion'):
                t = TarifaHorayFraccion(tarifa = tmonto)
            t.save()
            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = HorarioEstacionamiento(horaIn, horaOut, reservaIn, reservaOut)
            if not m_validado[0]:
                return render(request, 'templateMensaje.html', {'color':'red', 'mensaje': m_validado[1]})
            # debería funcionar con excepciones

            estacionamiento.tarifa = tmonto
            estacionamiento.apertura = horaIn
            estacionamiento.cierre = horaOut
            estacionamiento.reservasInicio = reservaIn
            estacionamiento.reservasCierre = reservaOut
            estacionamiento.esquemaTarifa = t
            estacionamiento.nroPuesto = form.cleaned_data['puestos']

            estacionamiento.save()
            form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'form2': form2, 'estacionamiento': estacionamiento})


def estacionamiento_reserva(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = EstacionamientoReserva()

    # Si es un POST estan mandando un request
    elif request.method == 'POST':
        form = EstacionamientoReserva(request.POST)
        # Verificamos si es valido con los validadores del formulario
        if form.is_valid():
            inicioReserva = form.cleaned_data['inicio']
            finalReserva = form.cleaned_data['final']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(inicioReserva, finalReserva, estacionamiento.reservasInicio, estacionamiento.reservasCierre)


            # Si no es valido devolvemos el request
            if not m_validado[0]:
                return render(request, 'templateMensaje.html', {'color':'red', 'mensaje': m_validado[1]})

            if marzullo(_id, inicioReserva, finalReserva):
                global reservaFinal
                reservaFinal = Reserva(estacionamiento=estacionamiento,inicioReserva=inicioReserva,finalReserva=finalReserva)
                monto = Decimal(estacionamiento.esquemaTarifa.calcularPrecio(inicioReserva,finalReserva))
                return render(request, 'estacionamientoPagarReserva.html', {'id': _id,'monto': monto,'reserva': reservaFinal,'color':'green', 'mensaje':'Existe un puesto disponible'})
            else:
                # Cambiar mensaje
                return render(request, 'templateMensaje.html', {'color':'red', 'mensaje':'No hay un puesto disponible para ese horario'})

    return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacionamiento})

def estacionamiento_pago(request,_id):
    form = PagoTarjetaDeCredito()
    if request.method == 'POST':
        form = PagoTarjetaDeCredito(request.POST)
        if form.is_valid():
            global reservaFinal
            reservaFinal.save()
            return render(request,'pago.html',{"id": _id, "color": "green",'mensaje' : "Se realizo el pago de reserva satisfactoriamente"})
    return render(request, 'pago.html', {'form':form})
