# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from django.forms.widgets import SplitDateTimeWidget

class CustomSplitDateTimeWidget(SplitDateTimeWidget):

    def format_output(self, rendered_widgets):
        return '<p></p>'.join(rendered_widgets)

class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
                        regex = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                        message = 'Debe introducir un formato válido.'
                    )

    # Nombre del dueno del estacionamiento (no se permiten digitos)
    propietario = forms.CharField(
                        required = True,
                        label = "Propietario",
                        validators = [
                             RegexValidator(
                                regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                                message = 'Sólo debe contener letras.'
                            )
                        ],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Propietario',
                            'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                            'message':'La entrada debe ser un nombre sin números.'
                        }
                    )
                )

    nombre = forms.CharField(
                        required = True,
                        label = "Nombre",
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Nombre',
                            'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                            'message':'La entrada debe ser un nombre sin números.'
                        }
                    )
                )

    direccion = forms.CharField(
                        required = True,
                        label = "Direccion",
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Direccion',
                            'message':'La entrada no puede quedar vacía.'
                        }
                    )
                )

    telefono_1 = forms.CharField(
                        required = False,
                        validators = [phone_validator],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Telefono 1',
                            'pattern':'^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                            'message':'La entrada debe ser un teléfono válido.'
                        }
                    )
                )

    telefono_2 = forms.CharField(
                        required = False,
                        validators = [phone_validator],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Telefono 2',
                            'pattern':'^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                            'message':'La entrada debe ser un teléfono válido.'
                        }
                    )
                )

    telefono_3 = forms.CharField(
                        required = False,
                        validators = [phone_validator],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Telefono 3',
                            'pattern':'^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                            'message':'La entrada debe ser un teléfono válido.'
                        }
                    )
                )

    email_1 = forms.EmailField(
                        required = False,
                        widget = forms.EmailInput(attrs = {
                            'class':'form-control',
                            'placeholder':'E-mail 1',
                            'message':'La entrada debe ser un e-mail válido.'
                        }
                    )
                )

    email_2 = forms.EmailField(
                        required = False,
                        widget = forms.EmailInput(attrs = {
                            'class':'form-control',
                            'placeholder':'E-mail 2',
                            'message':'La entrada debe ser un e-mail válido.'
                        }
                    )
                )

    rif = forms.CharField(
                        required = True,
                        label = "RIF",
                        validators = [
                            RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido.'
                            )
                        ],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'RIF: J-xxxxxxxxx',
                            'pattern':'^[JVD]-\d{8}-?\d$',
                            'message':'La entrada debe ser un RIF válido'
                        }
                    )
                )

class EstacionamientoExtendedForm(forms.Form):
    puestos = forms.IntegerField(
                        required = True,
                        min_value = 0,
                        label = 'Número de Puestos',
                        widget = forms.NumberInput(attrs= {
                            'class':'form-control',
                            'placeholder':'Número de Puestos',
                            'min':"0", 'pattern':'^[0-9]+',
                            'message':'La entrada debe ser un número no negativo.'
                        }
                    )
                )

    tarifa_validator = RegexValidator(
                        regex = '^([0-9]+(\.[0-9]+)?)$',
                        message = 'Sólo debe contener dígitos.'
                    )

    horarioin = forms.TimeField(
                        required = True,
                        label = 'Horario Apertura',
                        widget = forms.TextInput(attrs = {'class':'form-control',
                            'placeholder':'Horario Apertura',
                            'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]',
                            'message':'La entrada debe ser una hora válida.'
                        }
                    )
                )

    horarioout = forms.TimeField(
                        required = True,
                        label = 'Horario Cierre',
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Horario Cierre',
                            'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]',
                            'message':'La entrada debe ser una hora válida.'
                        }
                    )
                )

    horario_reserin = forms.TimeField(
                        required = True,
                        label = 'Horario Inicio Reserva',
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Horario Inicio Reserva',
                            'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]',
                            'message':'La entrada debe ser una hora válida.'
                        }
                    )
                )

    horario_reserout = forms.TimeField(
                        required = True, label = 'Horario Fin Reserva',
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Horario Fin Reserva',
                            'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]',
                            'message':'La entrada debe ser una hora válida.'
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
        choices = choices_esquema,
        widget = forms.Select(attrs = {'class':'form-control'})
    )

    tarifa = forms.DecimalField(
                        required = True,
                        validators = [tarifa_validator],
                        widget = forms.TextInput(attrs = {'class':'form-control',
                            'placeholder':'Tarifa',
                            'pattern':'^([0-9]+(\.[0-9]+)?)$',
                            'message':'La entrada debe ser un número decimal.'
                        }
                    )
                )

    tarifa2 = forms.DecimalField(
                        required = False,
                        validators = [tarifa_validator],
                        widget = forms.TextInput(attrs = {'class':'form-control',
                            'placeholder':'Tarifa 2',
                            'pattern':'^([0-9]+(\.[0-9]+)?)$',
                            'message':'La entrada debe ser un número decimal.'
                        }
                    )
                )

    inicioTarifa2 = forms.TimeField(
                        required = False,
                        label = 'Inicio Horario Especial',
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Horario Inicio Reserva',
                            'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]',
                            'message':'La entrada debe ser una hora válida.'
                        }
                    )
                )

    finTarifa2 = forms.TimeField(
                        required = False,
                        label = 'Fin Horario Especial',
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Horario Fin Reserva',
                            'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]',
                            'message':'La entrada debe ser una hora válida.'
                        }
                    )
                )

class ReservaForm(forms.Form):
    inicio = forms.SplitDateTimeField(
                        required = True,
                        label = 'Horario Inicio Reserva',
                        widget= CustomSplitDateTimeWidget(attrs={
                            'class':'form-control',
                            'type':'date',
                            'placeholder':'Hora Inicio Reserva'
                        }
                    )
                )

    final = forms.SplitDateTimeField(
                        required = True,
                        label = 'Horario Final Reserva',
                        widget = CustomSplitDateTimeWidget(attrs={
                            'class':'form-control',
                            'type':'date',
                            'placeholder':'Hora Final Reserva'
                        }
                    )
                )

class PagoForm(forms.Form):

    nombre = forms.CharField(
                        required = True,
                        label = "Nombre",
                        validators = [
                            RegexValidator(
                                regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
                            )
                        ],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Nombre',
                            'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                            'message':'La entrada no puede contener números o empezar con espacios en blanco.'
                        }
                    )
                )

    apellido = forms.CharField(
                        required = True,
                        label = "Apellido",
                        validators = [
                            RegexValidator(
                                regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos')
                        ],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Apellido',
                            'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                            'message':'La entrada no puede contener números o empezar con espacios en blanco.'
                        }
                    )
                )

    cedulaTipo = forms.ChoiceField(
                        required = True,
                        label = 'cedulaTipo',
                        choices = (
                            ('V', 'V'),
                            ('E', 'E')
                        )
                    )

    cedula = forms.CharField(
                        required = True,
                        label = "Cédula",
                        validators = [
                            RegexValidator(
                                regex = '^[0-9]+$',
                                message = 'La cédula solo puede contener caracteres numéricos')
                            ],
                        widget = forms.TextInput(attrs = {
                            'placeholder':'Cédula',
                            'pattern':'^[0-9]+$',
                            'message':'La entrada debe ser un número de cédula válido.',
                            'maxlength':'9'
                        }
                    )
                )

    tarjetaTipo = forms.ChoiceField(
                        required = True,
                        label = 'tarjetaTipo',
                        choices = (
                            ('Vista',  ' VISTA '),
                            ('Mister', ' MISTER '),
                            ('Xpress', ' XPRESS ')
                        ),
                        widget = forms.RadioSelect()
                    )

    tarjeta = forms.CharField(
                        required = True,
                        label = "Tarjeta de Credito",
                        validators = [
                            RegexValidator(
                                regex = '^[0-9]{16}$',
                                message = 'Introduzca un número de tarjeta válido.'
                            )
                        ],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'Tarjeta de Credito',
                            'pattern':'^[0-9]{16}$',
                            'message':'La entrada debe ser un número de tarjeta válido.'
                        }
                    )
                )

class RifForm(forms.Form):
        rif = forms.CharField(
                        required = True,
                        label = "RIF",
                        validators = [
                            RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido.'
                            )
                        ],
                        widget = forms.TextInput(attrs = {
                            'class':'form-control',
                            'placeholder':'RIF: J-xxxxxxxxx',
                            'pattern':'^[JVD]-\d{8}-?\d$',
                            'message':'La entrada debe ser un RIF válido'
                        }
                    )
                )