# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import urllib
from django.http import HttpResponse, Http404
from django.utils.dateparse import parse_datetime
from urllib.parse import urlencode
from matplotlib import pyplot
from decimal import Decimal
from collections import OrderedDict

from datetime import (
    datetime,
)

from estacionamientos.controller import (
    HorarioEstacionamiento,
    validarHorarioReserva,
    marzullo,
    get_client_ip,
    tasa_reservaciones,
    calcular_porcentaje_de_tasa,
    consultar_ingresos,
    splitDates, 
)

from estacionamientos.forms import (
    PorcentajeForm,
    EstacionamientoExtendedForm,
    PropietarioForm,
    BilleteraElectronicaForm,
    ValidarBilleteraForm,
    EstacionamientoForm,
    ReservaForm,
    PagoForm,
    RifForm,
    CedulaForm,
    ConsultarSaldoForm,
    RecargarSaldoForm,
    CambiarPropietarioForm,
    CancelarReservaForm,
    AgregarDiaFeriado
    )

from estacionamientos.models import (
    SAGE,
    Estacionamiento,
    Propietario,
    BilleteraElectronica,
    Reserva,
    Pago,
    DiasFeriados,
    TarifaHora,
    TarifaMinuto,
    TarifaHorayFraccion,
    TarifaFinDeSemana,
    TarifaHoraPico,
    HistorialBilleteraElectronica)

def tarifa_cancelacion(request):

    try:
        tarifaCan = SAGE.objects.get(id = 1)
    except ObjectDoesNotExist:
        tarifaCan = SAGE(tarifa_cancelacion = 0.0)

    if request.method == 'GET':

        form_data = {'porcentaje': tarifaCan.tarifa_cancelacion}
        form = PorcentajeForm(data = form_data)

    elif request.method == 'POST':

        form = PorcentajeForm(request.POST)
        if form.is_valid():
            tarifaCan.tarifa_cancelacion = form.cleaned_data['porcentaje']
            tarifaCan.save()
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'green'
                , 'mensaje' : 'Porcentaje cambiado satisfactoriamente'
                }
            )
        else: #Esto nunca deberia pasar de todas formas
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'Error en los argumentos de la forma'
                }
            )

    return render(
        request,
        'administracion.html',
        { 'form': form }
    )

# Usamos esta vista para procesar todos los estacionamientos
def estacionamientos_all(request):
    estacionamientos = Estacionamiento.objects.all()

    # Si es un GET, mandamos un formulario vacio
    if request.method == 'GET':
        form  = EstacionamientoForm()
    # Si es POST, se verifica la información recibida
    elif request.method == 'POST':
        # Creamos un formulario con los datos que recibimos
        form  = EstacionamientoForm(request.POST)
        # Parte de la entrega era limitar la cantidad maxima de
        # estacionamientos a 5
        if len(estacionamientos) >= 5:
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'No se pueden agregar más estacionamientos'
                }
            )

        # Si el formulario es valido, entonces creamos un objeto con
        # el constructor del modelo
        if form.is_valid():
            try: 
                objetoPropietario = Propietario.objects.get(ci = form.cleaned_data['ci_propietario'])
                
                obj = Estacionamiento(
                    ci_propietario  = objetoPropietario,
                    nombre          = form.cleaned_data['nombre'],
                    direccion       = form.cleaned_data['direccion'],
                    rif             = form.cleaned_data['rif'],
                    telefono1       = form.cleaned_data['telefono_1'],
                    telefono2       = form.cleaned_data['telefono_2'],
                    telefono3       = form.cleaned_data['telefono_3'],
                    email1          = form.cleaned_data['email_1'],
                    email2          = form.cleaned_data['email_2']
                )
                obj.save()    
                est = Estacionamiento.objects.get(rif = form.cleaned_data['rif'])                         
                dia = DiasFeriados(
                    idest = est.id,
                    fecha = '2016-07-05',
                    descripcion = "Declaracion de la independencia"
                )
                dia.save()
                dia2 = DiasFeriados(
                    idest = est.id,
                    fecha = '2016-04-19',
                    descripcion = "Firma del acta de independencia"
                )
                dia2.save()
                dia3 = DiasFeriados(
                    idest = est.id,
                    fecha = '2016-05-01',
                    descripcion = "Dia del trabajador"
                )
                dia3.save()
                dia4 = DiasFeriados(
                    idest = est.id,
                    fecha = '2015-06-24',
                    descripcion = "Batalla de Carabobo"
                )
                dia4.save()
                dia5 = DiasFeriados(
                    idest = est.id,
                    fecha = '2015-12-31',
                    descripcion = "Ultimo dia del año"
                )
                dia5.save()
                dia6 = DiasFeriados(
                    idest = est.id,
                    fecha = '2016-01-01',
                    descripcion = "Primer dia del año"
                )
                dia6.save()
                dia7 = DiasFeriados(
                    idest = est.id,
                    fecha = '2015-10-12',
                    descripcion = "Dia de la raza"
                )
                dia7.save()
                dia8 = DiasFeriados(
                    idest = est.id,
                    fecha = '2015-12-24',
                    descripcion = "Navidad"
                )
                dia8.save()
                # Recargamos los estacionamientos ya que acabamos de agregar
                estacionamientos = Estacionamiento.objects.all()
                form = EstacionamientoForm()
            
            except:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'CI no pertenece a ningun propietario.'
                    }
                )
            
    return render(
        request,
        'catalogo-estacionamientos.html',
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
        raise Http404

    if request.method == 'GET':
        if estacionamiento.tarifa:
            form_data = {
                'horarioin'             : estacionamiento.apertura,
                'horarioout'            : estacionamiento.cierre,
                'tarifa_motos'          : estacionamiento.tarifa.tarifa_motos,
                'tarifa_carros'         : estacionamiento.tarifa.tarifa_carros,
                'tarifa_camiones'       : estacionamiento.tarifa.tarifa_camiones,
                'tarifa_microbus'       : estacionamiento.tarifa.tarifa_microbus,
                'tarifa_autobus'        : estacionamiento.tarifa.tarifa_autobus,
                'tarifa_especiales'     : estacionamiento.tarifa.tarifa_especiales,
                'tarifa2_motos'         : estacionamiento.tarifa.tarifa2_motos,
                'tarifa2_carros'        : estacionamiento.tarifa.tarifa2_carros,
                'tarifa2_camiones'      : estacionamiento.tarifa.tarifa2_camiones,
                'tarifa2_microbus'      : estacionamiento.tarifa.tarifa2_microbus,
                'tarifa2_autobus'       : estacionamiento.tarifa.tarifa2_autobus,
                'tarifa2_especiales'    : estacionamiento.tarifa.tarifa2_especiales,
                'tarifa3_motos'         : estacionamiento.tarifa2.tarifa_motos,
                'tarifa3_carros'        : estacionamiento.tarifa2.tarifa_carros,
                'tarifa3_camiones'      : estacionamiento.tarifa2.tarifa_camiones,
                'tarifa3_microbus'      : estacionamiento.tarifa2.tarifa_microbus,
                'tarifa3_autobus'       : estacionamiento.tarifa2.tarifa_autobus,
                'tarifa3_especiales'    : estacionamiento.tarifa2.tarifa_especiales,
                'tarifa4_motos'         : estacionamiento.tarifa2.tarifa2_motos,
                'tarifa4_carros'        : estacionamiento.tarifa2.tarifa2_carros,
                'tarifa4_camiones'      : estacionamiento.tarifa2.tarifa2_camiones,
                'tarifa4_microbus'      : estacionamiento.tarifa2.tarifa2_microbus,
                'tarifa4_autobus'       : estacionamiento.tarifa2.tarifa2_autobus,
                'tarifa4_especiales'    : estacionamiento.tarifa2.tarifa2_especiales,
                'inicioTarifa2'         : estacionamiento.tarifa2.inicioEspecial,
                'finTarifa2'            : estacionamiento.tarifa2.finEspecial,
                'puestos_motos'         : estacionamiento.capacidad_motos,
                'puestos_carros'        : estacionamiento.capacidad_carros,
                'puestos_camiones'      : estacionamiento.capacidad_camiones,
                'puestos_microbus'      : estacionamiento.capacidad_microbus,
                'puestos_autobus'       : estacionamiento.capacidad_autobus,
                'puestos_especiales'    : estacionamiento.capacidad_especiales,
                'esquema'               : estacionamiento.tarifa.__class__.__name__,
                'horizonte_reserva'     : estacionamiento.horizonte_reserva,
                'inicioTarifaFeriado2'  : estacionamiento.tarifa2.inicioEspecial,
                'finTarifaFeriado2'     : estacionamiento.tarifa2.finEspecial,
                'esquema2'              : estacionamiento.tarifa2.__class__.__name__
            }
            form = EstacionamientoExtendedForm(data = form_data)
        else:
            form = EstacionamientoExtendedForm()

    elif request.method == 'POST':
        # Leemos el formulario
        form = EstacionamientoExtendedForm(request.POST)
        # Si el formulario
        if form.is_valid():
            horaIn                = form.cleaned_data['horarioin']
            horaOut               = form.cleaned_data['horarioout']
            tarifa_motos          = form.clean_tarifa('tarifa_motos')
            tarifa_carros         = form.clean_tarifa('tarifa_carros')
            tarifa_camiones       = form.clean_tarifa('tarifa_camiones')
            tarifa_microbus       = form.clean_tarifa('tarifa_microbus')
            tarifa_autobus        = form.clean_tarifa('tarifa_autobus')
            tarifa_especiales     = form.clean_tarifa('tarifa_especiales')
            horizonte             = form.clean_horizonte()
            tipo                  = form.cleaned_data['esquema']
            tipo2                 = form.cleaned_data['esquema2']
            inicioTarifa2         = form.cleaned_data['inicioTarifa2']
            finTarifa2            = form.cleaned_data['finTarifa2']
            inicioTarifaFeriado2  = form.cleaned_data['inicioTarifaFeriado2']
            finTarifaFeriado2     = form.cleaned_data['finTarifaFeriado2']
            tarifa2_motos         = form.clean_tarifa('tarifa2_motos')
            tarifa2_carros        = form.clean_tarifa('tarifa2_carros')
            tarifa2_camiones      = form.clean_tarifa('tarifa2_camiones')
            tarifa2_microbus      = form.clean_tarifa('tarifa2_microbus')
            tarifa2_autobus       = form.clean_tarifa('tarifa2_autobus')
            tarifa2_especiales    = form.clean_tarifa('tarifa2_especiales')
            tarifa3_motos         = form.clean_tarifa('tarifa3_motos')
            tarifa3_carros        = form.clean_tarifa('tarifa3_carros')
            tarifa3_camiones      = form.clean_tarifa('tarifa3_camiones')
            tarifa3_microbus      = form.clean_tarifa('tarifa3_microbus')
            tarifa3_autobus       = form.clean_tarifa('tarifa3_autobus')
            tarifa3_especiales    = form.clean_tarifa('tarifa3_especiales')
            tarifa4_motos         = form.clean_tarifa('tarifa4_motos')
            tarifa4_carros        = form.clean_tarifa('tarifa4_carros')
            tarifa4_camiones      = form.clean_tarifa('tarifa4_camiones')
            tarifa4_microbus      = form.clean_tarifa('tarifa4_microbus')
            tarifa4_autobus       = form.clean_tarifa('tarifa4_autobus')
            tarifa4_especiales    = form.clean_tarifa('tarifa4_especiales')

            esquemaTarifa = eval(tipo)(
                tarifa_motos         = tarifa_motos,
                tarifa_carros        = tarifa_carros,
                tarifa_camiones      = tarifa_camiones,
                tarifa_microbus      = tarifa_microbus,
                tarifa_autobus       = tarifa_autobus,
                tarifa_especiales    = tarifa_especiales,
                tarifa2_motos        = tarifa2_motos,
                tarifa2_carros       = tarifa2_carros,
                tarifa2_camiones     = tarifa2_camiones,
                tarifa2_microbus     = tarifa2_microbus,
                tarifa2_autobus      = tarifa2_autobus,
                tarifa2_especiales   = tarifa2_especiales,
                inicioEspecial       = inicioTarifa2,
                finEspecial          = finTarifa2
            )
            
            esquemaTarifa2 = eval(tipo2)(
                tarifa_motos         = tarifa3_motos,
                tarifa_carros        = tarifa3_carros,
                tarifa_camiones      = tarifa3_camiones,
                tarifa_microbus      = tarifa3_microbus,
                tarifa_autobus       = tarifa3_autobus,
                tarifa_especiales    = tarifa3_especiales,
                tarifa2_motos        = tarifa4_motos,
                tarifa2_carros       = tarifa4_carros,
                tarifa2_camiones     = tarifa4_camiones,
                tarifa2_microbus     = tarifa4_microbus,
                tarifa2_autobus      = tarifa4_autobus,
                tarifa2_especiales   = tarifa4_especiales,
                inicioEspecial       = inicioTarifaFeriado2,
                finEspecial          = finTarifaFeriado2
            )

            esquemaTarifa.save()
            esquemaTarifa2.save()

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            if not HorarioEstacionamiento(horaIn, horaOut):
                return render(
                    request,
                    'template-mensaje.html',
                    { 'color':'red'
                    , 'mensaje': 'El horario de apertura debe ser menor al horario de cierre'
                    }
                )
            # debería funcionar con excepciones
            estacionamiento.tarifa               = esquemaTarifa
            estacionamiento.tarifa2              = esquemaTarifa2
            estacionamiento.apertura             = horaIn
            estacionamiento.cierre               = horaOut
            estacionamiento.capacidad_motos      = form.clean_puestos('puestos_motos')
            estacionamiento.capacidad_carros     = form.clean_puestos('puestos_carros')
            estacionamiento.capacidad_camiones   = form.clean_puestos('puestos_camiones')
            estacionamiento.capacidad_microbus   = form.clean_puestos('puestos_microbus')
            estacionamiento.capacidad_autobus    = form.clean_puestos('puestos_autobus')
            estacionamiento.capacidad_especiales = form.clean_puestos('puestos_especiales')
            estacionamiento.horizonte_reserva    = horizonte
            estacionamiento.capacidad            = (estacionamiento.capacidad_motos +
                                                    estacionamiento.capacidad_carros +
                                                    estacionamiento.capacidad_camiones +
                                                    estacionamiento.capacidad_microbus +
                                                    estacionamiento.capacidad_autobus +
                                                    estacionamiento.capacidad_especiales)

            if estacionamiento.capacidad == 0:
                return render(
                    request,
                    'template-mensaje.html',
                    { 'color':'red'
                    , 'mensaje': 'El estacionamiento debe tener al menos un puesto'
                    }
                )

            estacionamiento.save()
            form = EstacionamientoExtendedForm()

    return render(
        request,
        'detalle-estacionamiento.html',
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
        raise Http404

    # Verificamos que el estacionamiento este parametrizado
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # Esta prohibido entrar aun

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = ReservaForm()

    # Si es un POST estan mandando un request
    elif request.method == 'POST':
        form = ReservaForm(request.POST)
        # Verificamos si es valido con los validadores del formulario
        if form.is_valid():

            inicioReserva = form.cleaned_data['inicio']
            finalReserva = form.cleaned_data['final']
            tipoVehiculo = form.cleaned_data['tipoVehiculo']

            # debería funcionar con excepciones, y el mensaje debe ser mostrado
            # en el mismo formulario
            m_validado = validarHorarioReserva(
                inicioReserva,
                finalReserva,
                estacionamiento.apertura,
                estacionamiento.cierre,
                estacionamiento.horizonte_reserva
            )

            # Si no es valido devolvemos el request
            if not m_validado[0]:
                return render(
                    request,
                    'template-mensaje.html',
                    { 'color'  :'red'
                    , 'mensaje': m_validado[1]
                    }
                )

            if marzullo(_id, inicioReserva, finalReserva, tipoVehiculo):
                reservaFinal = Reserva(
                    nombre          = form.cleaned_data['nombre'],
                    apellido        = form.cleaned_data['apellido'],
                    ci              = form.cleaned_data['ci'],
                    estacionamiento = estacionamiento,
                    inicioReserva   = inicioReserva,
                    finalReserva    = finalReserva,
                    tipoVehiculo    = tipoVehiculo
                )
                
                listaDias = DiasFeriados.objects.filter(idest = _id)
                tipoDias = splitDates(inicioReserva,finalReserva,listaDias)
                monto = 0
                for intervalo in tipoDias[0]:                    
                    monto += estacionamiento.tarifa.calcularPrecio(intervalo[0],intervalo[1],tipoVehiculo)
                for intervalo2 in tipoDias[1]:
                    monto += estacionamiento.tarifa2.calcularPrecio(intervalo2[0],intervalo2[1],tipoVehiculo)

                monto = Decimal(monto)

                request.session['monto']               = float(monto)
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
                request.session['tipoVehiculo']        = tipoVehiculo
                request.session['nombre']              = form.cleaned_data['nombre']
                request.session['apellido']            = form.cleaned_data['apellido']
                request.session['ci']                  = form.cleaned_data['ci']

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
                return render(
                    request,
                    'template-mensaje.html',
                    {'color'   : 'red'
                    , 'mensaje' : 'No hay un puesto disponible para ese horario'
                    }
                )

    return render(
        request,
        'reserva.html',
        { 'form': form
        , 'estacionamiento': estacionamiento
        }
    )
    
def estacionamiento_cancelar_reserva(request):
        
    if request.method == 'GET': 
        form = CancelarReservaForm()
        
    if request.method == 'POST': 
        form = CancelarReservaForm(request.POST)
        
        if form.is_valid():
            idReserva = form.cleaned_data['idReserva']
            ci        = form.cleaned_data['cedula']
            
            #Intenta conseguir la reserva
            try:    
                pagoReserva = Pago.objects.get(id = idReserva)
            except ObjectDoesNotExist:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Id no existe o CI no corresponde al registrado en el recibo de pago'
                    }
                )
        
            #Verifica que sea la cedula correcta
            if pagoReserva.reserva.ci != ci:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Id no existe o CI no corresponde al registrado en el recibo de pago'
                    }
                )
                
            #Guarda la información del pago y de la reserva    
            request.session['idPagoReserva'] = pagoReserva.id
            request.session['idReserva']     = pagoReserva.reserva.id
        
            #Forma para verificar la billetera a recargar 
            billetera = ValidarBilleteraForm()
            return render(
                request,
                'cancelar-info-billetera.html',
                { 'billetera' : billetera }
            )
        
    return render(
        request,
        'cancelar.html',
        { 'form': form
        }
    )
    
#Recibe el 'post' luego de introducir la billetera
def estacionamiento_cancelar_reserva_billetera(request): 

    if request.method == 'POST':
    
        form = ValidarBilleteraForm(request.POST)
        #Guarda lo que introdujo el usuario
        if form.is_valid():
            identificador = form.cleaned_data['idValid']
            pinVal = form.cleaned_data['pinValid']
            #Busca la billetera en la base de datos    
            try:    
                billetera = BilleteraElectronica.objects.get(idBilletera = identificador)
            except ObjectDoesNotExist:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Autenticación denegada'
                    }
                )
            
            #Verifica que el PIN sea el correcto    
            if pinVal != billetera.PIN:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Autenticación denegada'
                    }
                )
       
        #Recoge la información del pago y reserva de la persona para borrarlos de la BD
        idPago    = request.session['idPagoReserva']
        idReserva = request.session['idReserva']
        
        pago    = Pago.objects.get(id = idPago)
        reserva = Reserva.objects.get(id = idReserva)
        
        #Verificación de que la reserva no esté en curso
        if ((reserva.finalReserva >= datetime.now()) and (datetime.now()>=reserva.inicioReserva)):
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'La reserva está en curso. No puede cancelarla'
                }
            )
            
        #Verificación de que la reserva no sea de una fecha pasada
        if (reserva.finalReserva < datetime.now()): 
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'La reserva ya pasó. No puede cancelarla'
                }
            )

        descuento = 0
        if pago.tipoPago == "Tarjeta":
            descuento = pago.monto*reserva.tarifa_cancelar.tarifa_cancelacion/100
        reembolzo = pago.monto - descuento

        #Verificando que sea posible abonar la billetera
        if (billetera.saldo + reembolzo > 10000):
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'Abonar a esta billetera no es posible ya que el saldo sobrepasaría los 10000. Por favor introduzca otra billetera'
                }
            )
        
        historial = HistorialBilleteraElectronica(
            billetera        = billetera,
            fechaTransaccion = datetime.now(),
            tipo             = "Cancelacion",
            nombre           = reserva.nombre,
            apellido         = reserva.apellido,
            cedula           = reserva.ci,
            credito          = reembolzo
            )
            
        historial.save()
        
        billetera.saldo += reembolzo
        billetera.save()
        pago.estado = False
        pago.save()
        reserva.delete()
        
        return render(
            request, 'factura-devolucion.html',
            { 'devolucion' : historial,
              'descuento' : descuento,
              'pago' : pago }
        )

def estacionamiento_pago(request,_id):
    form = PagoForm()
    
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404
    
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # No esta permitido acceder a esta vista aun
    
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            
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

            tipoVehiculo = request.session['tipoVehiculo']

            try:
                tarifaCan = SAGE.objects.get(id = 1)
            except ObjectDoesNotExist:
                tarifaCan = SAGE(tarifa_cancelacion = 0.0)
                tarifaCan.save()

            reservaFinal = Reserva(
                nombre          = request.session['nombre'],
                apellido        = request.session['apellido'],
                ci              = request.session['ci'],
                estacionamiento = estacionamiento,
                tarifa_cancelar = tarifaCan,
                inicioReserva   = inicioReserva,
                finalReserva    = finalReserva,
                tipoVehiculo    = tipoVehiculo
            )

            # Se guarda la reserva en la base de datos
            reservaFinal.save()

            monto = Decimal(request.session['monto']).quantize(Decimal('1.00'))
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = form.cleaned_data['cedula'],
                monto            = monto,
                tipoPago         = "Tarjeta",
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
    
def estacionamiento_pago_billetera(request,_id):
    form = ValidarBilleteraForm()
    
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404
    
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # No esta permitido acceder a esta vista aun
    
    if request.method == 'POST':
    
        form = ValidarBilleteraForm(request.POST)
        #Guarda lo que introdujo el usuario
        if form.is_valid():
            identificador = form.cleaned_data['idValid']
            pinVal = form.cleaned_data['pinValid']
            #Busca la billetera en la base de datos    
            try:    
                billetera = BilleteraElectronica.objects.get(idBilletera = identificador)
            except ObjectDoesNotExist:
                return render(
                    request, 'template-mensaje-popup.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Autenticación denegada'
                    }
                )
            
            #Verifica que el PIN sea el correcto    
            if pinVal != billetera.PIN:
                return render(
                    request, 'template-mensaje-popup.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Autenticación denegada'
                    }
                )
            
            monto = Decimal(request.session['monto']).quantize(Decimal('1.00'))
            if billetera.saldo < monto:
                return render(
                    request, 'template-mensaje-popup.html',
                    { 'color'   : 'black'
                    , 'mensaje' : 'Saldo insuficiente '
                    }
                )
          
            billetera.saldo -= monto 
            billetera.save() #Actualiza el saldo
            
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

            tipoVehiculo = request.session['tipoVehiculo']

            try:
                tarifaCan = SAGE.objects.get(id = 1)
            except ObjectDoesNotExist:
                tarifaCan = SAGE(tarifa_cancelacion = 0.0)
                tarifaCan.save()

            reservaFinal = Reserva(
                nombre          = request.session['nombre'],
                apellido        = request.session['apellido'],
                ci              = request.session['ci'],                   
                estacionamiento = estacionamiento,
                tarifa_cancelar = tarifaCan,
                inicioReserva   = inicioReserva,
                finalReserva    = finalReserva,
                tipoVehiculo    = tipoVehiculo
            )

            # Se guarda la reserva en la base de datos
            reservaFinal.save()
            
            pago = Pago(
                fechaTransaccion = datetime.now(),
                cedula           = billetera.CI,
                monto            = monto,
                tipoPago         = "Billetera",
                reserva          = reservaFinal,
            )

            # Se guarda el recibo de pago en la base de datos
            pago.save()
            
            historial = HistorialBilleteraElectronica(
                billetera        = billetera,
                fechaTransaccion = datetime.now(),
                tipo             = "Reserva",
                nombre           = request.session['nombre'],
                apellido         = request.session['apellido'],
                cedula           = request.session['ci'],
                debito           = monto
                )
            
            historial.save()
            
            return render(
                request,
                'pago_billetera.html',
                { "id"       : _id
                , "pago"     : pago
                , "billetera": billetera
                , "color"    : "green"
                , 'mensaje'  : "Se realizo el pago de reserva satisfactoriamente."
                }
            )

    return render(
        request,
        'pago_billetera.html',
        { 'form' : form
        }
    )

def estacionamiento_ingreso(request):
    form = RifForm()
    if request.method == 'POST':
        form = RifForm(request.POST)
        if form.is_valid():

            rif = form.cleaned_data['rif']
            listaIngresos, ingresoTotal = consultar_ingresos(rif)

            return render(
                request,
                'consultar-ingreso.html',
                { "ingresoTotal"  : ingresoTotal
                , "listaIngresos" : listaIngresos
                , "form"          : form
                }
            )

    return render(
        request,
        'consultar-ingreso.html',
        { "form" : form }
    )

def estacionamiento_consulta_reserva(request):
    form = CedulaForm()
    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula        = form.cleaned_data['cedula']
            facturas      = Pago.objects.filter(estado = True).filter(reserva__ci = cedula)
            listaFacturas = []

            listaFacturas = sorted(
                list(facturas),
                key = lambda r: r.reserva.inicioReserva
            )
            return render(
                request,
                'consultar-reservas.html',
                { "listaFacturas" : listaFacturas
                , "form"          : form
                }
            )
    return render(
        request,
        'consultar-reservas.html',
        { "form" : form }
    )

def receive_sms(request):
    ip = get_client_ip(request) # Busca el IP del telefono donde esta montado el SMS Gateway
    port = '8000' # Puerto del telefono donde esta montado el SMS Gateway
    phone = request.GET.get('phone', False)
    sms = request.GET.get('text', False)
    if (not sms or not phone):
        return HttpResponse(status=400) # Bad request
    
    phone = urllib.parse.quote(str(phone)) # Codificacion porcentaje del numero de telefono recibido
    
    # Tratamiento del texto recibido
    try:
        sms = sms.split(' ')
        id_sms = int(sms[0])
        inicio_reserva = sms[1] + ' ' + sms[2]
        final_reserva = sms[3] + ' ' + sms[4]
        inicio_reserva = parse_datetime(inicio_reserva)
        final_reserva = parse_datetime(final_reserva)
    except:
        return HttpResponse(status=400) # Bad request
    
    # Validacion del id de estacionamiento recibido por SMS
    try:
        estacionamiento = Estacionamiento.objects.get(id = id_sms)
    except ObjectDoesNotExist:
        text = 'No existe el estacionamiento ' + str(id_sms) + '.'
        text = urllib.parse.quote(str(text))
        urllib.request.urlopen('http://{0}:{1}/sendsms?phone={2}&text={3}&password='.format(ip, port, phone, text))
        return HttpResponse('No existe el estacionamiento ' + str(id_sms) + '.')
    
    # Validacion de las dos fechas recibidas por SMS
    m_validado = validarHorarioReserva(
        inicio_reserva,
        final_reserva,
        estacionamiento.apertura,
        estacionamiento.cierre,
    )
    if m_validado[0]:
        '''reserva_sms = Reserva(
            estacionamiento = estacionamiento,
            inicioReserva   = inicio_reserva,
            finalReserva    = final_reserva,
        )
        reserva_sms.save()'''
        text = 'Se realizó la reserva satisfactoriamente.'
        text = urllib.parse.quote(str(text))
        urllib.request.urlopen('http://{0}:{1}/sendsms?phone={2}&text={3}&password='.format(ip, port, phone, text))
    else:
        text = m_validado[1]
        text = urllib.parse.quote(str(text))
        urllib.request.urlopen('http://{0}:{1}/sendsms?phone={2}&text={3}&password='.format(ip, port, phone, text))
        return HttpResponse(m_validado[1])
    
    return HttpResponse('')
    
def tasa_de_reservacion(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404
    if (estacionamiento.apertura is None):
        return render(
            request, 'template-mensaje.html',
            { 'color'   : 'red'
            , 'mensaje' : 'Se debe parametrizar el estacionamiento primero.'
            }
        )
    ocupacion = tasa_reservaciones(_id)
    calcular_porcentaje_de_tasa(estacionamiento.apertura, estacionamiento.cierre, estacionamiento.capacidad, ocupacion)
    datos_ocupacion = urlencode(ocupacion) # Se convierten los datos del diccionario en el formato key1=value1&key2=value2&...
    return render(
        request,
        'tasa-reservacion.html',
        { "ocupacion" : ocupacion
        , "datos_ocupacion": datos_ocupacion
        }
    )

def grafica_tasa_de_reservacion(request):
    
    # Recuperacion del diccionario para crear el grafico
    try:
        datos_ocupacion = request.GET.dict()
        datos_ocupacion = OrderedDict(sorted((k, float(v)) for k, v in datos_ocupacion.items()))     
        response = HttpResponse(content_type='image/png')
    except:
        return HttpResponse(status=400) # Bad request
    
    # Si el request no viene con algun diccionario
    if (not datos_ocupacion):
        return HttpResponse(status=400) # Bad request
    
    # Configuracion y creacion del grafico de barras con la biblioteca pyplot
    pyplot.switch_backend('Agg') # Para que no use Tk y aparezcan problemas con hilos
    pyplot.bar(range(len(datos_ocupacion)), datos_ocupacion.values(), hold = False, color = '#6495ed')
    pyplot.ylim([0,100])
    pyplot.title('Distribución de los porcentajes por fecha')
    pyplot.xticks(range(len(datos_ocupacion)), list(datos_ocupacion.keys()), rotation=20)
    pyplot.ylabel('Porcentaje (%)')
    pyplot.grid(True, 'major', 'both')
    pyplot.savefig(response, format='png') # Guarda la imagen creada en el HttpResponse creado
    pyplot.close()
    
    return response

def propietarios_all(request):
    propietarios = Propietario.objects.all()

    # Si es un GET, mandamos un formulario vacio
    if request.method == 'GET':
        form = PropietarioForm() 
        
    # Si es POST, se verifica la información recibida
    elif request.method == 'POST':
        # Creamos un formulario con los datos que recibimos
        form = PropietarioForm(request.POST)
        
        if form.is_valid():
            obj = Propietario(
                nombre   = form.cleaned_data['nombreProp'],
                apellido = form.cleaned_data['apellidoProp'],
                ci       = form.cleaned_data['ci'],
                tel      = form.cleaned_data['telefono']
            )
            obj.save()
            propietarios = Propietario.objects.all()
            form = PropietarioForm()
            
    return render(
        request,
        'catalogo-propietarios.html',
        { 'form': form
        , 'propietarios': propietarios
        }
    )
    
def cambiar_propietario(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacionamiento = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        raise Http404

    # Verificamos que el estacionamiento este parametrizado
    if (estacionamiento.apertura is None):
        return HttpResponse(status = 403) # Esta prohibido entrar aun

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = CambiarPropietarioForm()

    # Si es un POST estan mandando un request
    elif request.method == 'POST':
        form = CambiarPropietarioForm(request.POST)
        # Verificamos si es valido con los validadores del formulario
        if form.is_valid():
            try:
                objetoPropietario = Propietario.objects.get(ci = form.cleaned_data['ci_propietario'])
                estacionamiento.ci_propietario = objetoPropietario
                estacionamiento.save()
            
            except:
                return render(
                    request,
                    'cambiar-propietario.html',
                    { 'form': form,
                      'estacionamiento' : estacionamiento,
                      'mensaje' : 'CI no pertenece a ningun propietario',
                      'color' : 'red'
                    }
                )
                
        return render(
            request,
            'cambiar-propietario.html',
            { 'form': form,
                'estacionamiento' : estacionamiento,
                'mensaje' : 'Cambio del propietario satisfactorio',
                'color' : 'green'
            }
        )
    
    return render(
        request,
        'cambiar-propietario.html',
        { 'form': form,
          'estacionamiento' : estacionamiento
        })

def billetera_electronica(request):
    
    if request.method =="GET":   
        form = ValidarBilleteraForm()
    
    #Si recibe los datos del usuario    
    if request.method == 'POST':
    
        form = ValidarBilleteraForm(request.POST)
        #Guarda lo que introdujo el usuario
        if form.is_valid():
            identificador = form.cleaned_data['idValid']
            pinVal = form.cleaned_data['pinValid']
            #Busca la billetera en la base de datos    
            try:    
                billetera = BilleteraElectronica.objects.get(idBilletera = identificador)
            except ObjectDoesNotExist:
                return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'Autenticación denegada'
                }
            )
            
            #Verifica que el PIN sea el correcto    
            if pinVal != billetera.PIN:
                return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'Autenticación denegada'
                }
            )

            if "saldo" in request.POST:
                return render(
                    request,
                    'billetera_electronica_saldo.html',
                    {'billetera' : billetera}
                )
            
            elif "historial" in request.POST:
                return render(
                    request,
                    'billetera_electronica_historial.html',
                    {'billetera' : billetera,
                     'historial' : HistorialBilleteraElectronica.objects.filter(billetera = billetera)}   
                )
                
    return render(
        request, 'Billetera-Electronica.html',
        {'form': form}
    )
    
def billetera_electronica_crear(request):
    billeteras = BilleteraElectronica.objects.all()
    
    if request.method == 'GET':
        form = BilleteraElectronicaForm()

    elif request.method == 'POST':
        
        form = BilleteraElectronicaForm(request.POST) 
        if form.is_valid():
            obj = BilleteraElectronica(
                nombre      = form.cleaned_data['nombreUsu'],
                apellido    = form.cleaned_data['apellidoUsu'],
                CI          = form.cleaned_data['ciUsu'],
                PIN         = form.cleaned_data['pinUsu'],
                idBilletera = len(billeteras),
                saldo       = 0
            )
            obj.save()
            billeteras = BilleteraElectronica.objects.all()
            form = BilleteraElectronicaForm()
            
    return render(
        request,
        'billetera_electronica_crear.html',
        { 'form': form
        , 'billeteras' : billeteras
        }
    )

#Intento de recargar saldo, view incompleto
def billetera_electronica_recargar(request):
    
    if request.method == 'GET':
        form = RecargarSaldoForm()
    if request.method == 'POST':
        form = RecargarSaldoForm(request.POST)
        #Guarda lo que introdujo el usuario
        if form.is_valid():
            identificador = form.cleaned_data['idBill']
            monto = form.cleaned_data['monto']
            pinVal = form.cleaned_data['pinValid']
            try:    
                billetera = BilleteraElectronica.objects.get(idBilletera = identificador)
            except ObjectDoesNotExist:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Autenticación denegada'
                    }
                )
                
            if pinVal != billetera.PIN:
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'Autenticación denegada'
                    }
                )
            
            if billetera.saldo + Decimal(monto) > 10000:
                resto = 10000 - billetera.saldo
                return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'La recarga excede el limite de 10.000. Solo puede recargar un maximo de ' + str(resto) + ' restante'
                }
                )
                
            if Decimal(monto) <= 0:
                return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'No puedes recargar este monto a la billetera'
                }
                )
                
            billetera.saldo += Decimal(monto)
            billetera.save()
            
            recarga = HistorialBilleteraElectronica(
                billetera        = billetera,
                fechaTransaccion = datetime.now(),
                tipo             = "Recarga",
                nombre           = form.cleaned_data['nombre'],
                apellido         = form.cleaned_data['apellido'],
                cedula           = form.cleaned_data['cedula'],
                tarjeta          = "****" + form.cleaned_data['tarjeta'][-4:],
                credito          = Decimal(form.cleaned_data['monto'])
                )
            
            recarga.save()
            
            return render(
                request, 'recarga.html',
                { 'color'     : 'black'  
                , 'pago'      : recarga     
                , 'billetera' : billetera       
                , 'mensaje'   : 'Su nuevo saldo es '+ str(billetera.saldo)
                }
            )
    
    return render(request,  
        'billetera_electronica_recarga.html',
        { 'form': form
        }
    )
    
def estacionamiento_feriados(request,_id):
    if request.method == 'POST':
        form = AgregarDiaFeriado(request.POST)       
        if form.is_valid():
            try:
                dia = DiasFeriados.objects.get(fecha = form.cleaned_data['dia'], idest = _id) 
                return render(
                    request, 'template-mensaje.html',
                    { 'color'   : 'red'
                    , 'mensaje' : 'La fecha introducida ya pertenece a los dias feriados'
                    }
                )              
            except ObjectDoesNotExist:       
                nuevoDia = DiasFeriados(
                    idest = _id,
                    fecha = form.cleaned_data['dia'],
                    descripcion = form.cleaned_data['descripcion']                  
                )
                nuevoDia.save()
    form = AgregarDiaFeriado()
    dias = DiasFeriados.objects.filter(idest = _id )
    return render(
        request, 'dias_feriados.html',
        { 'form'    : form
        , 'id'      : _id
        , 'dias'    :  dias               
        }
    )
    
def estacionamiento_feriados_remover(request,_id,_idrem):
    if _idrem :
        try:
            dia = DiasFeriados.objects.get(id = _idrem)
            dia.delete()
        except:
            return render(
                request, 'template-mensaje.html',
                { 'color'   : 'red'
                , 'mensaje' : 'La fecha introducida no pertenece a los dias feriados'
                }
            )
    form = AgregarDiaFeriado()
    dias = DiasFeriados.objects.filter(idest = _id )
    return render(
        request, 'dias_feriados.html',
        { 'form'    : form
        , 'id'      : _id
        , 'dias'    :  dias               
        }
    )
