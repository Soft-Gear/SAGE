# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from estacionamientos.controller import *
from estacionamientos.forms import EstacionamientoExtendedForm
from estacionamientos.forms import EstacionamientoForm
from estacionamientos.forms import EstacionamientoReserva
from estacionamientos.forms import PagoTarjetaDeCredito
from estacionamientos.models import Estacionamiento, ReservasModel

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

    elif request.method == 'POST':
        # Leemos el formulario
        form = EstacionamientoExtendedForm(request.POST)
        # Si el formulario
        if form.is_valid():
            horaIn = form.cleaned_data['horarioin']
            horaOut = form.cleaned_data['horarioout']
            reservaIn = form.cleaned_data['horario_reserin']
            reservaOut = form.cleaned_data['horario_reserout']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = HorarioEstacionamiento(horaIn, horaOut, reservaIn, reservaOut)
            if not m_validado[0]:
                return render(request, 'templateMensaje.html', {'color':'red', 'mensaje': m_validado[1]})
            # debería funcionar con excepciones

            estacionamiento.tarifa = form.cleaned_data['tarifa']
            estacionamiento.apertura = horaIn
            estacionamiento.cierre = horaOut
            estacionamiento.reservasInicio = reservaIn
            estacionamiento.reservasCierre = reservaOut
            estacionamiento.nroPuesto = form.cleaned_data['puestos']

            estacionamiento.save()
            form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacionamiento})


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
            inicio_reserva = form.cleaned_data['inicio']
            final_reserva = form.cleaned_data['final']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(inicio_reserva, final_reserva, estacionamiento.Reservas_Inicio, estacionanmiento.Reservas_Cierre)

            # Si no es valido devolvemos el request
            if not m_validado[0]:
                return render(request, 'templateMensaje.html', {'color':'red', 'mensaje': m_validado[1]})




            # Si esta en un rango valido, procedemos a buscar en la lista
            # el lugar a insertar
            x = buscar(inicio_reserva, final_reserva, listaReserva)
            if x[2] == True :
                reservar(inicio_reserva, final_reserva, listaReserva)
                reservaFinal = ReservasModel(
                                    Estacionamiento = estacion,
                                    Puesto = x[0],
                                    InicioReserva = inicio_reserva,
                                    FinalReserva = final_reserva
                                )
                reservaFinal.save()
                return render(request, 'templateMensaje.html', {'color':'green', 'mensaje':'Se realizo la reserva exitosamente'})
            else:
                return render(request, 'templateMensaje.html', {'color':'red', 'mensaje':'No hay un puesto disponible para ese horario'})

    return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacion})

def estacionamiento_pago(request,_id):
    form = PagoTarjetaDeCredito()
    if request.method == 'POST':
        form = PagoTarjetaDeCredito(request.POST)
        print (request.POST['numeroTarjeta'])
        if form.is_valid():
            return render(request,'pago.html',{"color": "green",'mensaje' : "Se realizo el pago de reserva satisfactoriamente"})
    return render(request, 'pago.html', {'form':form})

