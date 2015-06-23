# -*- coding: utf-8 -*-

from django.test import TestCase

from decimal import Decimal

from datetime import (
    datetime,
    time
)

from estacionamientos.models import (
    TarifaMinuto,
    TarifaHora,
    TarifaHorayFraccion,
    TarifaFinDeSemana,
    TarifaHoraPico
)
        


###################################################################
# Casos de prueba de tipos de tarifa
###################################################################

class DecimalTestCase(TestCase):

    # Casos de decimales

    def test_tarifa_hora_motos_decimal(self):
        rate=TarifaHora(tarifa_motos=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,0)
        vehiculo = 'Moto'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.9'))

    def test_tarifa_hora_carros_decimal(self):
        rate=TarifaHora(tarifa_carros=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,0)
        vehiculo ='Carro'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.9'))

    def test_tarifa_hora_camiones_decimal(self):
        rate=TarifaHora(tarifa_camiones=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,0)
        vehiculo ='Camion'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.9'))

    def test_tarifa_hora_especiales_decimal(self):
        rate=TarifaHora(tarifa_especiales=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,0)
        vehiculo ='Vehículo Especial'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.9'))

    def test_tarifa_minuto_motos_decimal(self):
        rate=TarifaMinuto(tarifa_motos=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,30)
        vehiculo = 'Moto'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('1.05'))

    def test_tarifa_minuto_carros_decimal(self):
        rate=TarifaMinuto(tarifa_carros=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,30)
        vehiculo = 'Carro'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('1.05'))

    def test_tarifa_minuto_camiones_decimal(self):
        rate=TarifaMinuto(tarifa_camiones=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,30)
        vehiculo = 'Camion'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('1.05'))

    def test_tarifa_minuto_especiales_decimal(self):
        rate=TarifaMinuto(tarifa_especiales=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,18,30)
        vehiculo = 'Vehículo Especial'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('1.05'))

    def test_tarifa_hora_y_fraccion_motos_decimal(self):
        rate=TarifaHorayFraccion(tarifa_motos=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,17,25)
        vehiculo = 'Moto'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.75'))

    def test_tarifa_hora_y_fraccion_carros_decimal(self):
        rate=TarifaHorayFraccion(tarifa_carros=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,17,25)
        vehiculo = 'Carro'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.75'))

    def test_tarifa_hora_y_fraccion_camiones_decimal(self):
        rate=TarifaHorayFraccion(tarifa_camiones=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,17,25)
        vehiculo = 'Camion'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.75'))

    def test_tarifa_hora_y_fraccion_especiales_decimal(self):
        rate=TarifaHorayFraccion(tarifa_especiales=0.3)
        initial_time=datetime(2015,2,20,15,0)
        final_time=datetime(2015,2,20,17,25)
        vehiculo = 'Vehículo Especial'
        value = rate.calcularPrecio(initial_time, final_time, vehiculo)
        self.assertEqual(value, Decimal('0.75'))
        
    def test_tarifa_pico_motos_decimal(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa_motos=0.1,tarifa2_motos=0.3,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,15)
        finReserva = datetime(2015,1,1,20)
        vehiculo = 'Moto'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))

    def test_tarifa_pico_carros_decimal(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa_carros=0.1,tarifa2_carros=0.3,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,15)
        finReserva = datetime(2015,1,1,20)
        vehiculo = 'Carro'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))

    def test_tarifa_pico_camiones_decimal(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa_camiones=0.1,tarifa2_camiones=0.3,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,15)
        finReserva = datetime(2015,1,1,20)
        vehiculo = 'Camion'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))

    def test_tarifa_pico_especiales_decimal(self):
        inicio = time(6,0)
        fin = time(18,0)
        tarifa = TarifaHoraPico(tarifa_especiales=0.1,tarifa2_especiales=0.3,inicioEspecial=inicio,finEspecial=fin)
        inicioReserva = datetime(2015,1,1,15)
        finReserva = datetime(2015,1,1,20)
        vehiculo = 'Vehículo Especial'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))
        
    def test_tarifa_fin_de_semana_motos_decimal(self):
        tarifa = TarifaFinDeSemana(tarifa_motos=0.1,tarifa2_motos=0.3)
        inicioReserva = datetime(2015,3,6,22)
        finReserva = datetime(2015,3,7,3)
        vehiculo = 'Moto'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))

    def test_tarifa_fin_de_semana_carros_decimal(self):
        tarifa = TarifaFinDeSemana(tarifa_carros=0.1,tarifa2_carros=0.3)
        inicioReserva = datetime(2015,3,6,22)
        finReserva = datetime(2015,3,7,3)
        vehiculo = 'Carro'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))

    def test_tarifa_fin_de_semana_camiones_decimal(self):
        tarifa = TarifaFinDeSemana(tarifa_camiones=0.1,tarifa2_camiones=0.3)
        inicioReserva = datetime(2015,3,6,22)
        finReserva = datetime(2015,3,7,3)
        vehiculo = 'Camion'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))

    def test_tarifa_fin_de_semana_especiales_decimal(self):
        tarifa = TarifaFinDeSemana(tarifa_especiales=0.1,tarifa2_especiales=0.3)
        inicioReserva = datetime(2015,3,6,22)
        finReserva = datetime(2015,3,7,3)
        vehiculo = 'Vehículo Especial'
        valor = tarifa.calcularPrecio(inicioReserva,finReserva,vehiculo)
        self.assertEqual(valor,Decimal('1.10'))