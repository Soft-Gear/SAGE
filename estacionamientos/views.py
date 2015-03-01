# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from decimal import Decimal
from datetime import (
    datetime,
)

from estacionamientos.controller import (
    HorarioEstacionamiento,
    validarHorarioReserva,
    marzullo
)
from estacionamientos.forms import (
    EstacionamientoExtendedForm,
    EstacionamientoForm,
    ReservaForm,
    PagoForm,
    RifForm,
    CedulaForm,
)
from estacionamientos.models import (
    Estacionamiento,
    Reserva,
    Pago,
    TarifaHora,
    TarifaMinuto,
    TarifaHorayFraccion,
    TarifaFinDeSemana,
    TarifaHoraPico
)

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
            return render(
                request, 'templateMensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'No se pueden agregar más estacionamientos'
                }
            )

        # Si el formulario es valido, entonces creamos un objeto con
        # el constructor del modelo
        if form.is_valid():
            obj = Estacionamiento(
                propietario = form.cleaned_data['propietario'],
                nombre      = form.cleaned_data['nombre'],
                direccion   = form.cleaned_data['direccion'],
                rif         = form.cleaned_data['rif'],
                telefono1   = form.cleaned_data['telefono_1'],
                telefono2   = form.cleaned_data['telefono_2'],
                telefono3   = form.cleaned_data['telefono_3'],
                email1      = form.cleaned_data['email_1'],
                email2      = form.cleaned_data['email_2']
            )
            obj.save()
            # Recargamos los estacionamientos ya que acabamos de agregar
            estacionamientos = Estacionamiento.objects.all()
            form = EstacionamientoForm()

    return render(
        request,
        'catalogoEst.html',
        { 'form': form
        , 'estacionamientos': estacionamientos
        }
    )

def estacionamiento_detail(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(
            request,
            '404.html'
        )

    if request.method == 'GET':
        form = EstacionamientoExtendedForm()

    elif request.method == 'POST':
        # Leemos el formulario
        form = EstacionamientoExtendedForm(request.POST)
        # Si el formulario
        if form.is_valid():
            horaIn        = form.cleaned_data['horarioin']
            horaOut       = form.cleaned_data['horarioout']
            tarifa        = form.cleaned_data['tarifa']
            tipo          = form.cleaned_data['esquema']
            inicioTarifa2 = form.cleaned_data['inicioTarifa2']
            finTarifa2    = form.cleaned_data['finTarifa2']
            tarifa2       = form.cleaned_data['tarifa2']

            esquemaTarifa = eval(tipo)(
                tarifa         = tarifa,
                tarifa2        = tarifa2,
                inicioEspecial = inicioTarifa2,
                finEspecial    = finTarifa2
            )

            esquemaTarifa.save()
            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            if not HorarioEstacionamiento(horaIn, horaOut):
                return render(
                    request,
                    'templateMensaje.html',
                    { 'color':'red'
                    , 'mensaje': 'El horario de apertura debe ser menor al horario de cierre'
                    }
                )
            # debería funcionar con excepciones
            estacionamiento.tarifa    = esquemaTarifa
            estacionamiento.apertura  = horaIn
            estacionamiento.cierre    = horaOut
            estacionamiento.nroPuesto = form.cleaned_data['puestos']

            estacionamiento.save()
            form = EstacionamientoExtendedForm()

    return render(
        request,
        'detalleEst.html',
        { 'form': form
        , 'estacionamiento': estacionamiento
        }
    )


def estacionamiento_reserva(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(
            request,
            '404.html'
        )

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = ReservaForm()

    # Si es un POST estan mandando un request
    elif request.method == 'POST':
        form = ReservaForm(request.POST)
        print(request.POST)
        # Verificamos si es valido con los validadores del formulario
        if form.is_valid():

            inicioReserva = form.cleaned_data['inicio']
            print(form.cleaned_data)
            finalReserva = form.cleaned_data['final']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(
                inicioReserva,
                finalReserva,
                estacionamiento.apertura,
                estacionamiento.cierre,
            )

            # Si no es valido devolvemos el request
            if not m_validado[0]:
                return render(
                    request,
                    'templateMensaje.html',
                    { 'color'  :'red'
                    , 'mensaje': m_validado[1]
                    }
                )

            if marzullo(_id, inicioReserva, finalReserva):
                reservaFinal = Reserva(
                    estacionamiento = estacionamiento,
                    inicioReserva   = inicioReserva,
                    finalReserva    = finalReserva,
                )

                monto = Decimal(
                    estacionamiento.tarifa.calcularPrecio(
                        inicioReserva,finalReserva
                    )
                )

                request.session['monto'] = float(
                    estacionamiento.tarifa.calcularPrecio(
                        inicioReserva,
                        finalReserva
                    )
                )
                request.session['finalReservaHora']    = finalReserva.hour
                request.session['finalReservaMinuto']  = finalReserva.minute
                request.session['inicioReservaHora']   = inicioReserva.hour
                request.session['inicioReservaMinuto'] = inicioReserva.minute
                request.session['anioinicial']         = inicioReserva.year
                request.session['mesinicial']          = inicioReserva.month
                request.session['diainicial']          = inicioReserva.day
                request.session['aniofinal']           = finalReserva.year
                request.session['mesfinal']            = finalReserva.month
                request.session['diafinal']            = finalReserva.day
                return render(
                    request,
                    'confirmar.html',
                    { 'id'      : _id
                    , 'monto'   : monto
                    , 'reserva' : reservaFinal
                    , 'color'   : 'green'
                    , 'mensaje' : 'Existe un puesto disponible'
                    }
                )
            else:
                # Cambiar mensaje
                return render(
                    request,
                    'templateMensaje.html',
                    {'color'   : 'red'
                    , 'mensaje' : 'No hay un puesto disponible para ese horario'
                    }
                )

    return render(
        request,
        'reservar.html',
        { 'form': form
        , 'estacionamiento': estacionamiento
        }
    )

def estacionamiento_pago(request,_id):
    form = PagoForm()
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            try:
                estacionamiento = Estacionamiento.objects.get(id = _id)
            except ObjectDoesNotExist:
                return render(
                    request,
                    '404.html'
                )
            inicioReserva = datetime(
                year   = request.session['anioinicial'],
                month  = request.session['mesinicial'],
                day    = request.session['diainicial'],
                hour   = request.session['inicioReservaHora'],
                minute = request.session['inicioReservaMinuto']
            )

            finalReserva  = datetime(
                year   = request.session['aniofinal'],
                month  = request.session['mesfinal'],
                day    = request.session['diafinal'],
                hour   = request.session['finalReservaHora'],
                minute = request.session['finalReservaMinuto']
            )

            reservaFinal = Reserva(
                estacionamiento = estacionamiento,
                inicioReserva   = inicioReserva,
                finalReserva    = finalReserva,
            )

            # Se guarda la reserva en la base de datos
            reservaFinal.save()

            monto = Decimal(request.session['monto']).quantize(Decimal('1.00'))
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = form.cleaned_data['cedula'],
                cedulaTipo       = form.cleaned_data['cedulaTipo'],
                monto            = monto,
                tarjetaTipo      = form.cleaned_data['tarjetaTipo'],
                reserva          = reservaFinal,
            )

            # Se guarda el recibo de pago en la base de datos
            pago.save()

            return render(
                request,
                'pago.html',
                { "id"      : _id
                , "pago"    : pago
                , "color"   : "green"
                , 'mensaje' : "Se realizo el pago de reserva satisfactoriamente."
                }
            )

    return render(
        request,
        'pago.html',
        { 'form' : form }
    )

def estacionamiento_ingreso(request):
    form = RifForm()
    if request.method == 'POST':
        form = RifForm(request.POST)
        if form.is_valid():

            rif                   = form.cleaned_data['rif']
            listaEstacionamientos = Estacionamiento.objects.filter(rif = rif)
            ingresoTotal          = 0
            listaIngresos         = []

            for estacionamiento in listaEstacionamientos:
                listaFacturas = models.Pago.objects.filter(
                    reserva__estacionamiento__nombre = estacionamiento.nombre
                )
                ingreso       = [estacionamiento.nombre, 0]
                for factura in listaFacturas:
                    ingreso[1] += factura.monto
                listaIngresos += [ingreso]
                ingresoTotal  += ingreso[1]

            return render(
                request,
                'consultarIngreso.html',
                { "ingresoTotal"  : ingresoTotal
                , "listaIngresos" : listaIngresos
                , "form"          : form
                }
            )

    return render(
        request,
        'consultarIngreso.html',
        { "form" : form }
    )

def estacionamiento_consulta_reserva(request):
    form = CedulaForm()
    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():

            cedula        = form.cleaned_data['cedula']
            facturas      = Pago.objects.filter(cedula = cedula)
            listaFacturas = []

            listaFacturas = sorted(
                list(facturas),
                key = lambda r: r.reserva.inicioReserva
            )

            return render(
                request,
                'consultarReservas.html',
                { "listaFacturas" : listaFacturas
                , "form"          : form
                }
            )
    return render(
        request,
        'consultarReservas.html',
        { "form" : form }
    )
