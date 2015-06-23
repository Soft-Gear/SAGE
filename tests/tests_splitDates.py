# -*- coding: utf-8 -*-

from django.test import TestCase

from datetime import datetime
from estacionamientos.controller import splitDates
from estacionamientos.models import DiasFeriados

class splitDatesTestCase(TestCase):
    
    #Borde
    def test_splitDates_sin_Feriado(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]
                                      , []]
                            )
            
    #Borde
    def test_splitDates_Un_Feriado_En_Medio(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            dia = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-05',
                        descripcion = "Prueba"
                    )
            dia.save()
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-05/00:00'),"%Y-%m-%d/%H:%M")]
                                      ,[datetime.strptime(('2015-07-06/00:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]
                                      ,[[datetime.strptime(('2015-07-05/00:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-06/00:00'),"%Y-%m-%d/%H:%M")]]]
                            )
            
    #Borde
    def test_splitDates_Un_Feriado_Primer_Dia(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            dia = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-29',
                        descripcion = "Prueba"
                    )
            dia.save()
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]
                                      ,[]]
                            )

    #Borde
    def test_splitDates_Un_Feriado_Ultimo_Dia(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            dia = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-08',
                        descripcion = "Prueba"
                    )
            dia.save()
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/00:00'),"%Y-%m-%d/%H:%M")]]
                                      ,[[datetime.strptime(('2015-07-08/00:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]]
                            )

    #Esquina
    def test_splitDates_Dos_Feriados_En_Bordes(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            dia1 = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-29',
                        descripcion = "Prueba"
                    )
            dia2 = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-08',
                        descripcion = "Prueba"
                    )
            dia1.save()
            dia2.save()
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/00:00'),"%Y-%m-%d/%H:%M")]]
                                      ,[[datetime.strptime(('2015-07-08/00:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]]
                            )
            
    #Esquina
    def test_splitDates_Dos_Feriados_Seguidos_Primeros_Dias(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            dia1 = DiasFeriados(
                        idest = 0,
                        fecha = '2016-06-29',
                        descripcion = "Prueba"
                    )
            dia2 = DiasFeriados(
                        idest = 0,
                        fecha = '2016-06-30',
                        descripcion = "Prueba"
                    )
            dia1.save()
            dia2.save()
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-07-01/00:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]
                                      ,[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-01/00:00'),"%Y-%m-%d/%H:%M")]]]
                            )    

    #Esquina
    def test_splitDates_Dos_Feriados_Seguidos_Ultimos_Dias(self):
            inicio = datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M")
            final  = datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")
            dia1 = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-07',
                        descripcion = "Prueba"
                    )
            dia2 = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-08',
                        descripcion = "Prueba"
                    )
            dia1.save()
            dia2.save()
            listaDiasFeriados = DiasFeriados.objects.all()
            result = splitDates(inicio,final,listaDiasFeriados)
            self.assertEqual(result, [[[datetime.strptime(('2015-06-29/8:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-07/00:00'),"%Y-%m-%d/%H:%M")]]
                                      ,[[datetime.strptime(('2015-07-07/00:00'),"%Y-%m-%d/%H:%M"),datetime.strptime(('2015-07-08/8:00'),"%Y-%m-%d/%H:%M")]]]
                            )

    #Cobertura
    def test_Print_Feriados(self):
            dia = DiasFeriados(
                        idest = 0,
                        fecha = '2016-07-07',
                        descripcion = "Prueba"
                    )
            self.assertEqual(str(dia),'0 2016-07-07 Prueba')