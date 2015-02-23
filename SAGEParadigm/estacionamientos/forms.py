# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from estacionamientos.controller import FindAllSubclasses
from django.forms.widgets import SplitDateTimeWidget
from estacionamientos.models import * # No tocar esta linea

class MySplitDateTimeWidget(SplitDateTimeWidget):
    
    def format_output(self, rendered_widgets):
        return u'<p></p>'.join(rendered_widgets)


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
                    ],
                    widget = forms.TextInput(attrs = {
                        'class':'form-control',
                        'placeholder':'Propietario',
                        'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                        'required':'true',
                        'message':'La entrada debe ser un nombre sin numeros.'
                    })
                )

    nombre = forms.CharField(required = True, label = "Nombre",
                            widget = forms.TextInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Nombre',
                                'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                                'required':'true',
                                'message':'La entrada debe ser un nombre sin numeros.'
                            })
                        )

    direccion = forms.CharField(required = True, label = "Direccion",
                            widget = forms.TextInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Direccion',
                                'required':'true',
                                'message':'La entrada no puede quedar vacia.'
                            })
                        )

    telefono_1 = forms.CharField(required = False, validators = [phone_validator],
                            widget = forms.TextInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Telefono 1',
                                'pattern':'^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                                'message':'La entrada debe ser un telefono valido.'
                            })
                        )
    
    telefono_2 = forms.CharField(required = False, validators = [phone_validator],
                            widget = forms.TextInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Telefono 2',
                                'pattern':'^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                                'message':'La entrada debe ser un telefono valido.'
                            })
                        )
    
    telefono_3 = forms.CharField(required = False, validators = [phone_validator],
                            widget = forms.TextInput(attrs = {
                                'class':'form-control',
                                'placeholder':'Telefono 3',
                                'pattern':'^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                                'message':'La entrada debe ser un telefono valido.'
                            })
                        )

    email_1 = forms.EmailField(required = False,
                            widget = forms.EmailInput(attrs = {
                                'class':'form-control',
                                'placeholder':'E-mail 1',
                                'message':'La entrada debe ser un e-mail valido.'
                            })
                        )
    
    email_2 = forms.EmailField(required = False,
                            widget = forms.EmailInput(attrs = {
                                'class':'form-control',
                                'placeholder':'E-mail 2',
                                'message':'La entrada debe ser un e-mail valido.'
                            })
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
                        'placeholder':'RIF',
                        'pattern':'^[JVD]-?\d{8}-?\d$',
                        'required':'true',
                        'message':'La entrada debe ser un RIF valido'
                    })
                )

class EstacionamientoExtendedForm(forms.Form):


    puestos = forms.IntegerField(required=True, min_value = 0, label = 'Número de Puestos',
                                    widget = forms.NumberInput(attrs= {    
                                        'class':'form-control', 
                                        'placeholder':'Número de Puestos', 
                                        'min':"0", 'pattern':'^[0-9]+', 
                                        'required':'true', 
                                        'message':'La entrada debe ser un numero no negativo.'}
                                        )
                                )

    tarifa_validator = RegexValidator(
                            regex = '^([0-9]+(\.[0-9]+)?)$',
                            message = 'Sólo debe contener dígitos.'
                        )

    horarioin = forms.TimeField(required = True, label = 'Horario Apertura',
                                widget = forms.NumberInput(attrs = {'class':'form-control', 
                                     'placeholder':'Horario Apertura', 
                                     'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]', 
                                     'required':'true', 
                                     'message':'La entrada debe ser una hora valida'})
                                )
    
    horarioout = forms.TimeField(required = True, label = 'Horario Cierre',
                                widget = forms.TextInput(attrs = {
                                      'class':'form-control', 
                                      'placeholder':'Horario Cierre', 
                                      'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]', 
                                      'required':'true', 
                                      'message':'La entrada debe ser una hora valida'})
                                )

    horario_reserin = forms.TimeField(required = True, label = 'Horario Inicio Reserva', 
                                    widget = forms.TextInput(attrs = {
                                                       'class':'form-control', 
                                                       'placeholder':'Horario Inicio Reserva', 
                                                       'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]', 
                                                       'required':'true', 
                                                       'message':'La entrada debe ser una hora valida'})  
                                    )
    
    horario_reserout = forms.TimeField(required = True, label = 'Horario Fin Reserva',
                                       widget = forms.TextInput(attrs = {'class':'form-control', 
                                                        'placeholder':'Horario Fin Reserva', 
                                                        'pattern':'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]', 
                                                        'required':'true', 
                                                        'message':'La entrada debe ser una hora valida'})
                                        )

    tarifa = forms.CharField(required = True, validators = [tarifa_validator], 
                                            widget = forms.TextInput(attrs = {'class':'form-control', 
                                              'placeholder':'Tarifa', 
                                              'pattern':'^([0-9]+(\.[0-9]+)?)$', 
                                              'required':'true', 
                                              'message':'La entrada debe ser un numero decimal'})
                            )
    
    lista_de_esquemas = FindAllSubclasses(EsquemaTarifario)
    choices_esquema = []
    for i in range(len(lista_de_esquemas)):
        choices_esquema.append((i,lista_de_esquemas[i][0].tipo(None)))
    esquema = forms.ChoiceField(
                                required = True,
                                choices = choices_esquema,
                                widget = forms.Select(attrs = {'class':'form-control'})
    )

class EstacionamientoReserva(forms.Form):
    inicio = forms.SplitDateTimeField(label = 'Horario Inicio Reserva',
                                        widget= MySplitDateTimeWidget(attrs={
                                                                             'class':'form-control', 
                                                                             'type':'date',
                                                                             'placeholder':'Hora Inicio Reserva'}
                                                                    )
                                    )
    
    final = forms.SplitDateTimeField(label = 'Horario Final Reserva',
                                     widget = MySplitDateTimeWidget(attrs={
                                                                           'class':'form-control', 
                                                                           'type':'date',
                                                                           'placeholder':'Hora Final Reserva'}
                                                                    )
                                     )

class PagoTarjetaDeCredito(forms.Form):
    nombre = forms.CharField( required = True, 
                            label = "Nombre",
                            validators = [ RegexValidator( 
                                       regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                       message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos'
                                       )
                                    ],
                            widget = forms.TextInput(attrs = {
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                        'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                        'required':'true',
                                        'message':'La entrada no puede contener numeros o estar vacia'
                                    }
                                )
                            )
    apellido = forms.CharField( required = True, 
                            label = "Apellido",
                            validators = [ RegexValidator( 
                                       regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                       message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos')
                                    ],
                            widget = forms.TextInput(attrs = {
                                        'class':'form-control',
                                        'placeholder':'Apellido',
                                        'pattern':'^[a-zA-ZáéíóúñÑÁÉÍÓÚ][a-zA-ZáéíóúñÑÁÉÍÓÚ ]*$',
                                        'required':'true',
                                        'message':'La entrada no puede contener numeros o estar vacia'
                                    }
                                )
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
                                ],
                        widget = forms.TextInput(attrs = {
                                        'placeholder':'Cédula',
                                        'pattern':'^[0-9]+$',
                                        'required':'true',
                                        'message':'La entrada debe ser un numero de cedula valido',
                                        'maxlength':'9'
                                    }
                                )
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
                                        regex = '^[0-9]{16}$',
                                        message = 'Introduzca un numero de tarjeta válido.'
                                )
                            ],
                            widget = forms.TextInput(attrs = {
                                    'class':'form-control',
                                    'placeholder':'Tarjeta de Credito',
                                    'pattern':'^[0-9]{16}$',
                                    'required':'true',
                                    'message':'La entrada debe ser un numero de tarjeta valido'
                                }
                            )
                        )
