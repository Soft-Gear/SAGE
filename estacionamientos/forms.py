# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from django.forms.widgets import SplitDateTimeWidget


class CustomSplitDateTimeWidget(SplitDateTimeWidget):

    def format_output(self, rendered_widgets):
        return '<p></p>'.join(rendered_widgets)

class PropietarioForm(forms.Form):
    
    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    phone_validator = RegexValidator(
        regex   = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
        message = 'Debe introducir un formato válido de teléfono.'
    )
    
    name_validator = RegexValidator(
        regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\- ]+$',
        message = 'La entrada debe ser un nombre en Español sin símbolos especiales.'
    )
    
    nombreProp = forms.CharField(
        required   = True,
        label      = "Nombre",
        validators = [name_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )
    
    telefono = forms.CharField(
        required   = True,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )
    
    ci = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'CI: V/E-xxxxxxxx'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )
    
class CambiarPropietarioForm(forms.Form):
    
    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    # CI del dueno del estacionamiento
    ci_propietario = forms.CharField(
        required   = True,
        label      = "Cedula del Propietario",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cedula del Propietario'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )
    
class BilleteraElectronicaForm(forms.Form):

    name_validator = RegexValidator(
        regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\- ]+$',
        message = 'La entrada debe ser un nombre en Español sin símbolos especiales.'
    )
    
    pin_validator = RegexValidator(
        regex   = '^\d{4}$',
        message = 'EL PIN debe ser 4 digitos'
    )
    
    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    nombreUsu = forms.CharField(
        required   = True,
        label      = "Nombre",
        validators = [name_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message

            }
        )
    )
    
    ciUsu = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'V/E-xxxxxxxx'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )
    
    pinUsu = forms.CharField(
        required   = True,
        label      = "PIN",
        validators = [pin_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'PIN'
            , 'pattern'     : pin_validator.regex.pattern
            , 'message'     : pin_validator.message
            }
        )
    )
    
class ValidarBilleteraForm(forms.Form):

    pin_validator = RegexValidator(
        regex   = '^[0-9]{4}$',
        message = 'EL PIN debe ser 4 digitos'
    )
    
    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'Introduzca un id de digitos sin caracteres'
    )
      
    idValid = forms.CharField(
        required   = True,
        label      = "ID",
        validators = [id_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )
       
    pinValid = forms.CharField(
        required   = True,
        label      = "PIN",
        validators = [pin_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'PIN'
            , 'pattern'     : pin_validator.regex.pattern
            , 'message'     : pin_validator.message
            }
        )
    )

class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
        regex   = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
        message = 'Debe introducir un formato válido de teléfono.'
    )
    
    name_validator = RegexValidator(
        regex   = '^[0-9A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\!\¡\#\'\- ]+$',
        message = 'La entrada debe ser un nombre en Español sin símbolos especiales.'
    )
    
    rif_validator = RegexValidator(
        regex   = '^[JVD]-\d{8}-?\d$',
        message = 'Introduzca un RIF con un formato válido de la forma J/V/D-xxxxxxxxx.'
    )

    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    # Nombre del dueno del estacionamiento (no se permiten digitos)
    ci_propietario = forms.CharField(
        required   = True,
        label      = "Cedula del Propietario",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cedula del Propietario'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )

    nombre = forms.CharField(
        required   = True,
        label      = "Nombre del Estacionamiento",
        validators = [name_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Estacionamiento'
            , 'pattern'     : name_validator.regex.pattern
            , 'message'     : name_validator.message
            }
        )
    )

    direccion = forms.CharField(
        required = True,
        label    = "Direccion",
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Dirección'
            , 'message'     : 'La entrada no puede quedar vacía.'
            }
        )
    )

    telefono_1 = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono 1'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    telefono_2 = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono 2'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    telefono_3 = forms.CharField(
        required   = False,
        validators = [phone_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Teléfono 3'
            , 'pattern'     : phone_validator.regex.pattern
            , 'message'     : phone_validator.message
            }
        )
    )

    email_1 = forms.EmailField(
        required = False,
        widget   = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'E-mail 1'
            , 'message'     : 'La entrada debe ser un e-mail válido.'
            }
        )
    )

    email_2 = forms.EmailField(
        required = False,
        widget   = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'E-mail 2'
            , 'message'     : 'La entrada debe ser un e-mail válido.'
            }
        )
    )

    rif = forms.CharField(
        required   = True,
        label      = "RIF",
        validators = [rif_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'RIF: J/V/D-xxxxxxxx'
            , 'pattern'     : rif_validator.regex.pattern
            , 'message'     : rif_validator.message
            }
        )
    )
    
class ConsultarSaldoForm(forms.Form):
    
    pin_validator = RegexValidator(
        regex   = '^\d{4}$',
        message = 'EL PIN debe ser 4 digitos'
    )
    
    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'Introduzca un id de digitos'
    )
    
    idBill = forms.CharField(
        required   = True,
        label      = "ID Billetera",
        validators = [id_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID Billetera'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )
    
    pinUsu = forms.CharField(
        required   = True,
        label      = "PIN",
        validators = [pin_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'PIN'
            , 'pattern'     : pin_validator.regex.pattern
            , 'message'     : pin_validator.message
            }
        )
    )
      
class RecargarSaldoForm(forms.Form):
    
    card_name_validator = RegexValidator(
        regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\-]+$',
        message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    card_surname_validator = RegexValidator(
        regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\-]+$',
        message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    pin_validator = RegexValidator(
        regex   = '^\d{4}$',
        message = 'EL PIN debe ser 4 digitos'
    )
    
    card_validator = RegexValidator(
        regex   = '^[0-9]{16}$',
        message = 'Introduzca un número de tarjeta válido de 16 dígitos.'
    )
    
    nombre = forms.CharField(
        required   = True,
        label      = "Nombre del Tarjetahabiente",
        validators = [card_name_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Tarjetahabiente'
            , 'pattern'     : card_name_validator.regex.pattern
            , 'message'     : card_name_validator.message
            }
        )
    )

    apellido = forms.CharField(
        required   = True,
        label      = "Apellido del Tarjetahabiente",
        validators = [card_surname_validator],
        widget     = forms.TextInput(attrs =
            { 'class'      : 'form-control'
            , 'placeholder' : 'Apellido del Tarjetahabiente'
            , 'pattern'     : card_surname_validator.regex.pattern
            , 'message'     : card_surname_validator.message
            }
        )
    )

    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )
    
    tarjetaTipo = forms.ChoiceField(
        required = True,
        label    = 'tarjetaTipo',
        choices  = (
            ('Vista',  ' VISTA '),
            ('Mister', ' MISTER '),
            ('Xpress', ' XPRESS ')
            
        ),
        widget   = forms.RadioSelect()
    )

    tarjeta = forms.CharField(
        required   = True,
        label      = "Tarjeta de Credito",
        validators = [card_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarjeta de Credito'
            , 'pattern'     : card_validator.regex.pattern
            , 'message'     : card_validator.message
            }
        )
    )
    
    idBill_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'Introduzca un id de digitos'
    )
    
    idBill = forms.CharField(
        required   = True,
        label      = "ID Billetera",
        validators = [idBill_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID Billetera'
            , 'pattern'     : idBill_validator.regex.pattern
            , 'message'     : idBill_validator.message
            }
        )
    )
    
    pinValid = forms.CharField(
        required   = True,
        label      = "PIN",
        validators = [pin_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'PIN'
            , 'pattern'     : pin_validator.regex.pattern
            , 'message'     : pin_validator.message
            }
        )
    )
    
    monto_validator = RegexValidator(
        regex   = '^([0-9]+(\.[0-9]{1,2})?)$',
        message = 'Introduzca un monto valido, menor a 10000'
    )
    
    monto = forms.CharField(
        required   = True,
        label      = "Monto",
        validators = [monto_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Monto'
            , 'pattern'     : monto_validator.regex.pattern
            , 'message'     : monto_validator.message
            }
        )
    )
        
class EstacionamientoExtendedForm(forms.Form):
    
    tarifa_validator = RegexValidator(
        regex   = '^([0-9]+(\.[0-9]+)?)$',
        message = 'Sólo debe contener dígitos.'
    )
    
    puestos_motos = forms.IntegerField(
        required  = False,
        min_value = 0,
        label     = 'Puestos para Motos',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Puestos para Motos'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    puestos_carros = forms.IntegerField(
        required  = False,
        min_value = 0,
        label     = 'Puestos para Carros',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Puestos para Carros'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    puestos_camiones = forms.IntegerField(
        required  = False,
        min_value = 0,
        label     = 'Puestos para Camiones',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Puestos para Camiones'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    puestos_microbus = forms.IntegerField(
        required  = False,
        min_value = 0,
        label     = 'Puestos para Microbuses',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Puestos para Microbuses'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    puestos_autobus = forms.IntegerField(
        required  = False,
        min_value = 0,
        label     = 'Puestos para Autobuses',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Puestos para Autobuses'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    puestos_especiales = forms.IntegerField(
        required  = False,
        min_value = 0,
        label     = 'Puestos para Vehículos Especiales',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Puestos para Vehículos Especiales'
            , 'min'         : "0"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )

    horarioin = forms.TimeField(
        required = True,
        label    = 'Horario Apertura',
        widget   = forms.TextInput(attrs =
            { 'class':'form-control'
            , 'placeholder' : 'Horario Apertura'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )

    horarioout = forms.TimeField(
        required = True,
        label    = 'Horario Cierre',
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horario Cierre'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )
    
    horizonte_reserva = forms.IntegerField(
        required  = False,
        min_value = 0,
        max_value = 15,
        label     = 'Horizonte de reservacion',
        widget    = forms.NumberInput(attrs=
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horizonte de reservacion'
            , 'min'         : "0"
            , 'max'         : "15"
            , 'pattern'     : '^[0-9]+'
            , 'message'     : 'La entrada debe ser un número entero no negativo.'
            }
        )
    )


    choices_esquema = [
        ('TarifaHora', 'Por hora'),
        ('TarifaMinuto', 'Por minuto'),
        ('TarifaHorayFraccion', 'Por hora y fracción'),
        ('TarifaHoraPico', 'Diferenciada por horario pico'),
        ('TarifaFinDeSemana', 'Diferenciada para fines de semana')
    ]

    esquema = forms.ChoiceField(
        required = True,
        choices  = choices_esquema,
        widget   = forms.Select(attrs =
            { 'class' : 'form-control' }
        )
    )

    tarifa_motos = forms.DecimalField(
        required   = False,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa para Motos'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa_carros = forms.DecimalField(
        required   = False,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa para Carros'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa_camiones = forms.DecimalField(
        required   = False,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa para Camiones'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa_microbus = forms.DecimalField(
        required   = False,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa para Microbuses'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa_autobus = forms.DecimalField(
        required   = False,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa para Autobuses'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa_especiales = forms.DecimalField(
        required   = False,
        validators = [tarifa_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarifa para Vehículos Especiales'
            , 'pattern'     : '^([0-9]+(\.[0-9]+)?)$'
            , 'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2_motos = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2 para Motos',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2_carros = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2 para Carros',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2_camiones = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2 para Camiones',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2_microbus = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2 para Microbuses',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2_autobus = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2 para Autobuses',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    tarifa2_especiales = forms.DecimalField(
            required   = False,
            validators = [tarifa_validator],
            widget     = forms.TextInput(attrs = {
                'class'       : 'form-control',
                'placeholder' : 'Tarifa 2 para Vehículos Especiales',
                'pattern'     : '^([0-9]+(\.[0-9]+)?)$',
                'message'     : 'La entrada debe ser un número decimal.'
            }
        )
    )

    inicioTarifa2 = forms.TimeField(
        required = False,
        label    = 'Inicio Horario Especial',
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horario Inicio Reserva'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )

    finTarifa2 = forms.TimeField(
        required = False,
        label    = 'Fin Horario Especial',
        widget   = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Horario Fin Reserva'
            , 'pattern'     : '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            , 'message'     : 'La entrada debe ser una hora válida.'
            }
        )
    )
    
    #Funcion auxiliar para obtener las tarifas, retornando 0 si el campo esta vacia
    def clean_tarifa(self, tipo_tarifa):
        tarifa = self.cleaned_data[tipo_tarifa]
        if tarifa is None:
            return 0    #Si no se llena el campo se retorna como tarifa 0
        return tarifa
    
    def clean_puestos(self, tipo_puesto):
        puestos = self.cleaned_data[tipo_puesto]
        if puestos is None:
            return 0    #Igual aqui pero con puestos, campo vacio se traduce a no puestos
        return puestos
    
    def clean_horizonte(self):
        horizonte = self.cleaned_data['horizonte_reserva']
        if horizonte is None:
            return 15   #Igual aqui de nuevo, pero con horizontes, si no es especificado returnar el maximo, 15 dias.
        return horizonte

class ReservaForm(forms.Form):
    
    inicio = forms.SplitDateTimeField(
        required = True,
        label    = 'Horario Inicio Reserva',
        widget   = CustomSplitDateTimeWidget(attrs=
            { 'class'       : 'form-control'
            , 'type'        : 'date'
            , 'placeholder' : 'Hora Inicio Reserva'
            }
        )
    )

    final = forms.SplitDateTimeField(
        required = True,
        label    = 'Horario Final Reserva',
        widget   = CustomSplitDateTimeWidget(attrs=
            { 'class'       : 'form-control'
            , 'type'        : 'date'
            , 'placeholder' : 'Hora Final Reserva'
            }
        )
    )

    choices_tipoVehiculo = [
        ('Moto', 'Moto'),
        ('Carro', 'Carro'),
        ('Camion', 'Camión'),
        ('Microbus', 'Microbús'),
        ('Autobus', 'Autobús'),
        ('Vehículo Especial','Vehículo Especial')
    ]

    tipoVehiculo = forms.ChoiceField(
        required = True,
        choices  = choices_tipoVehiculo,
        widget   = forms.Select(attrs =
            { 'class' : 'form-control' }
        )
    )

class PagoForm(forms.Form):
    
    card_name_validator = RegexValidator(
        regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\-]+$',
        message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    card_surname_validator = RegexValidator(
        regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\-]+$',
        message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    card_validator = RegexValidator(
        regex   = '^[0-9]{16}$',
        message = 'Introduzca un número de tarjeta válido de 16 dígitos.'
    )
    
    nombre = forms.CharField(
        required   = True,
        label      = "Nombre del Tarjetahabiente",
        validators = [card_name_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Nombre del Tarjetahabiente'
            , 'pattern'     : card_name_validator.regex.pattern
            , 'message'     : card_name_validator.message
            }
        )
    )

    apellido = forms.CharField(
        required   = True,
        label      = "Apellido del Tarjetahabiente",
        validators = [card_surname_validator],
        widget     = forms.TextInput(attrs =
            { 'class'      : 'form-control'
            , 'placeholder' : 'Apellido del Tarjetahabiente'
            , 'pattern'     : card_surname_validator.regex.pattern
            , 'message'     : card_surname_validator.message
            }
        )
    )

    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )

    tarjetaTipo = forms.ChoiceField(
        required = True,
        label    = 'tarjetaTipo',
        choices  = (
            ('Vista',  ' VISTA '),
            ('Mister', ' MISTER '),
            ('Xpress', ' XPRESS ')
            
        ),
        widget   = forms.RadioSelect()
    )

    tarjeta = forms.CharField(
        required   = True,
        label      = "Tarjeta de Credito",
        validators = [card_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Tarjeta de Credito'
            , 'pattern'     : card_validator.regex.pattern
            , 'message'     : card_validator.message
            }
        )
    )

class RifForm(forms.Form):
    
    rif_validator = RegexValidator(
        regex   = '^[JVD]-\d{8}-?\d$',
        message = 'Introduzca un RIF con un formato válido de la forma J/V/D-xxxxxxxxx.'                              
    )
    
    rif = forms.CharField(
        required   = True,
        label      = "RIF",
        validators = [rif_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'RIF: J/V/D-xxxxxxxxx'
            , 'pattern'     : rif_validator.regex.pattern
            , 'message'     : rif_validator.message
            }
        )
    )

class CedulaForm(forms.Form):
    
    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )
    
class CancelarReservaForm(forms.Form):

    ci_validator = RegexValidator(
        regex   = '^[VE]-[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma V/E-xxxxxxxx.'
    )
    
    id_validator = RegexValidator(
        regex   = '^[0-9]+$',
        message = 'Introduzca un id de digitos'
    )
    
    cedula = forms.CharField(
        required   = True,
        label      = "Cédula",
        validators = [ci_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'Cédula'
            , 'pattern'     : ci_validator.regex.pattern
            , 'message'     : ci_validator.message
            }
        )
    )
    
    idReserva = forms.CharField(
        required   = True,
        label      = "ID",
        validators = [id_validator],
        widget     = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID Pago'
            , 'pattern'     : id_validator.regex.pattern
            , 'message'     : id_validator.message
            }
        )
    )
