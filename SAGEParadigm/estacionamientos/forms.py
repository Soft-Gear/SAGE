# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator


class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
                            regex = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                            message = 'Debe introducir un formato válido.'
                        )

    # nombre del dueno (no se permiten digitos)
    propietario = forms.CharField(
                    required = True,
                    label = "Propietario",
                    validators = [
                          RegexValidator(
                                regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                                message = 'Sólo debe contener letras.'
                        )
                    ]
                )

    nombre = forms.CharField(required = True, label = "Nombre")

    direccion = forms.CharField(required = True)

    telefono_1 = forms.CharField(required = False, validators = [phone_validator])
    telefono_2 = forms.CharField(required = False, validators = [phone_validator])
    telefono_3 = forms.CharField(required = False, validators = [phone_validator])

    email_1 = forms.EmailField(required = False)
    email_2 = forms.EmailField(required = False)

    rif = forms.CharField(
                    required = True,
                    label = "RIF",
                    validators = [
                          RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido.'
                        )
                    ]
                )

class EstacionamientoExtendedForm(forms.Form):


    puestos = forms.IntegerField(min_value = 0, label = 'Número de Puestos')

    tarifa_validator = RegexValidator(
                            regex = '^([0-9]+(\.[0-9]+)?)$',
                            message = 'Sólo debe contener dígitos.'
                        )

    horarioin = forms.TimeField(required = True, label = 'Horario Apertura')
    horarioout = forms.TimeField(required = True, label = 'Horario Cierre')

    horario_reserin = forms.TimeField(required = True, label = 'Horario Inicio Reserva')
    horario_reserout = forms.TimeField(required = True, label = 'Horario Fin Reserva')

    tarifa = forms.CharField(required = True, validators = [tarifa_validator])
    
class EstacionamientoExtendedForm2(forms.Form):
    
    choices_esquema = (
                       ('Por hora', 'hora'),
                       ('Por minuto', 'minuto'),
                       ('Por fraccion', 'fraccion')
    )
    
    esquema = forms.ChoiceField(
                                required = True,
                                choices = choices_esquema
    )

class EstacionamientoReserva(forms.Form):
    inicio = forms.TimeField(label = 'Horario Inicio Reserva')
    final = forms.TimeField(label = 'Horario Final Reserva')

class PagoTarjetaDeCredito(forms.Form):
    nombre = forms.CharField( required = True, 
                            label = "Nombre",
                            validators = [ RegexValidator( 
                                       regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                       message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos'
                                       )
                                    ]
                            )
    apellido = forms.CharField( required = True, 
                            label = "Apellido",
                            validators = [ RegexValidator( 
                                       regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                       message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos')
                                    ]
                            )
    cedulaTipo = forms.ChoiceField(required = True,
                                label = 'cedulaTipo',
                                choices = (
                                    ('V', 'V'),
                                    ('E', 'E')
                                )                       
                            )
    cedula = forms.CharField( required = True, 
                        label = "Cédula",
                        validators = [ RegexValidator( 
                                   regex = '^[0-9]+$',
                                   message = 'La cédula solo puede contener caracteres numéricos')
                                ]
                        )

    tarjetaTipo = forms.ChoiceField(required = True,
                                label = 'tarjetaTipo',
                                choices = (
                                    ('Vista', ' VISTA '),
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
                                        regex = '^[0-9]+$',
                                        message = 'Introduzca un numero de tarjeta válido.'
                                )
                            ]
                        )
