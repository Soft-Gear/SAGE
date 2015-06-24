# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import time

from estacionamientos.forms import EstacionamientoExtendedForm

###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

class ExtendedFormTestCase(TestCase):

    # malicia
    def test_estacionamiento_extended_form_un_campo(self):
        form_data = { 'puestos_motos': 2}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_dos_campos(self):
        form_data = { 'puestos_carros': 2,
                      'horarioin': time(hour = 6,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_tres_campos(self):
        form_data = { 'puestos_motos': 2,
                      'horarioin': time( hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0)}
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())
        
    # Malicia
    def test_estacionamiento_extended_form_cuatro_bien(self):
        form_data = { 'puestos_carros': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 12
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_estacionamiento_extended_form_cinco_campos_bien(self):
        form_data = { 'puestos_motos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'tarifa': 12,
                      'esquema':'TarifaMinuto'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # caso borde
    def test_estacionamiento_extended_form_seis_campos_bien(self):
        form_data = { 'puestos_motos': 2,
                      'horarioin': time(hour = 6,  minute = 0),
                      'horarioout': time(hour = 19,  minute = 0),
                      'esquema2' : 'TarifaHora',
                      'tarifa': 12,
                      'esquema':'TarifaHora'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #TDD
    def test_estacionamiento_extended_form_todos_los_campos_correctos_por_hora(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'horizonte_reserva' : 7,
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema':'TarifaHora',
                    'esquema2' : 'TarifaHora'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #TDD
    def test_estacionamiento_extended_form_todos_los_campos_correctos_por_minuto(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema':'TarifaMinuto',
                    'esquema2' : 'TarifaMinuto'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #TDD
    def test_estacionamiento_extended_form_todos_los_campos_correctos_por_hora_fraccion(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema':'TarifaHorayFraccion',
                    'esquema2' : 'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #TDD
    def test_estacionamiento_extended_form_todos_los_campos_correctos_por_hora_pico(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHoraPico',
                    'tarifa2_motos': 12,
                    'tarifa2_carros': 12,
                    'tarifa2_camiones': 12,
                    'tarifa2_especiales': 12,
                    'inicioTarifa2' : time(hour = 10,  minute = 0),
                    'finTarifa2'    : time(hour = 12,  minute = 0),
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid()) 

    #TDD
    def test_estacionamiento_extended_form_todos_los_campos_correctos_por_fin_semana(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaFinDeSemana',
                    'tarifa2_motos': 12,
                    'tarifa2_carros': 12,
                    'tarifa2_camiones': 12,
                    'tarifa2_especiales': 12,
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_puestos_motos_1(self):
        form_data = { 'puestos_motos': 1,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_puestos_carros_1(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 1,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #Borde
    def test_estacionamiento_extended_form_puestos_camiones_1(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 1,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_puestos_especiales_1(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 1,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
#---------------------------------------------------------------------------------------------------------------------------------------
    #Borde
    def test_estacionamiento_extended_form_muchos_puestos_motos(self):
        form_data = { 'puestos_motos': 2^31-1,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_motos'),2^31-1)

    #Borde
    def test_estacionamiento_extended_form_muchos_puestos_carros(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2^31-1,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_carros'),2^31-1)
        
    #Borde
    def test_estacionamiento_extended_form_muchos_puestos_camiones(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2^31-1,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_camiones'),2^31-1)

    #Borde
    def test_estacionamiento_extended_form_muchos_puestos_especiales(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2^31-1,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_especiales'),2^31-1)
#---------------------------------------------------------------------------------------------------------------------------------------
        #Borde
    def test_estacionamiento_extended_form_puestos_motos_0(self):
        form_data = { 'puestos_motos': 0,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_puestos_carros_0(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 0,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #Borde
    def test_estacionamiento_extended_form_puestos_camiones_0(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 0,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_puestos_especiales_0(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 0,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
#---------------------------------------------------------------------------------------------------------------------------------------
    #Borde
    def test_estacionamiento_extended_form_puestos_motos_nulos(self):
        form_data = { 'puestos_motos': None,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_motos'),0)

    #Borde
    def test_estacionamiento_extended_form_puestos_carros_nulos(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': None,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_carros'),0)
        
    #Borde
    def test_estacionamiento_extended_form_puestos_camiones_nulos(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': None,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_camiones'),0)

    #Borde
    def test_estacionamiento_extended_form_puestos_especiales_nulos(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': None,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_puestos('puestos_especiales'),0)
#---------------------------------------------------------------------------------------------------------------------------------------

    #Esquina
    def test_estacionamiento_extended_form_solo_un_puesto(self):
        form_data = { 'puestos_motos': 0,
                    'puestos_carros': 1,
                    'puestos_camiones': 0,
                    'puestos_especiales': 0,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Esquina
    def test_estacionamiento_extended_form_ningun_puesto(self):
        form_data = { 'puestos_motos': 0,
                    'puestos_carros': 0,
                    'puestos_camiones': 0,
                    'puestos_especiales': 0,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    # caso borde
    def test_estacionamiento_extended_form_hora_inicio_igual_hora_cierre(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 6,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_string_en_campo_puesto(self):
        form_data = { 'puestos_motos': "Hola",
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())

    # malicia
    def test_estacionamiento_extended_form_string_hora_inicio(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': "hola",
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertFalse(form.is_valid())
#---------------------------------------------------------------------------------------------------------------------------------------
    #Borde
    def test_estacionamiento_extended_form_tarifa_motos_grande(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 2^31-1,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_motos'),2^31-1)

    #Borde
    def test_estacionamiento_extended_form_tarifa_carros_grande(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 2^31-1,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_carros'),2^31-1)
        
    #Borde
    def test_estacionamiento_extended_form_tarifa_camiones_grande(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 2^31-1,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_camiones'),2^31-1)

    #Borde
    def test_estacionamiento_extended_form_tarifa_especiales_grande(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 2^31-1,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_especiales'),2^31-1)
#---------------------------------------------------------------------------------------------------------------------------------------
    #Borde
    def test_estacionamiento_extended_form_tarifa_motos_nula(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': None,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_motos'),0)

    #Borde
    def test_estacionamiento_extended_form_tarifa_carros_nula(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': None,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_carros'),0)
        
    #Borde
    def test_estacionamiento_extended_form_tarifa_camiones_nula(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': None,
                    'tarifa_especiales': 12,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_camiones'),0)

    #Borde
    def test_estacionamiento_extended_form_tarifa_especiales_nula(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_autobus': 2,
                    'puestos_microbus': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': 12,
                    'tarifa_carros': 12,
                    'tarifa_autobus': 12,
                    'tarifa_microbus': 12,
                    'tarifa_camiones': 12,
                    'tarifa_especiales': None,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tarifa('tarifa_especiales'),0)
#---------------------------------------------------------------------------------------------------------------------------------------
    # malicia
    def test_estacionamiento_extended_form_none_en_tarifa(self):
        form_data = { 'puestos_motos': 2,
                    'puestos_carros': 2,
                    'puestos_camiones': 2,
                    'puestos_especiales': 2,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'tarifa_motos': None,
                    'tarifa_carros': None,
                    'tarifa_camiones': None,
                    'tarifa_especiales': None,
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_horizonte_minimo(self):
        form_data = { 'horizonte_reserva' : 0,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())

    #Borde
    def test_estacionamiento_extended_form_horizonte_maximo(self):
        form_data = { 'horizonte_reserva' : 15,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        
    #Borde
    def test_estacionamiento_extended_form_horizonte_nulo(self):
        form_data = { 'horizonte_reserva' : None,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.clean_horizonte(),15)
        
    #Borde
    def test_estacionamiento_extended_form_horizonte_valido(self):
        form_data = { 'horizonte_reserva' : 1,
                    'horarioin': time(hour = 6,  minute = 0),
                    'horarioout': time(hour = 19,  minute = 0),
                    'esquema2' : 'TarifaHora',
                    'esquema':'TarifaHorayFraccion'
                    }
        form = EstacionamientoExtendedForm(data = form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.clean_horizonte(),1)
