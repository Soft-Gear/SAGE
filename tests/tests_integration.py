# -*- coding: utf-8 -*-

from django.test import Client
from django.test import TestCase

from datetime import time

from estacionamientos.models import (
                                        Estacionamiento,
                                        Propietario
                                    )

###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class IntegrationTest(TestCase):
    
    # TDD
    def setUp(self):
        self.client = Client()
        
    def crear_estacionamiento(self, puestos,hora_apertura=time(0,0),hora_cierre=time(23,59)):
        pro = Propietario(
            nombre = "Pablo",
            ci = 'V-12345678',
            tel = "0412-1234567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            #capacidad = puestos,
            #apertura       = hora_apertura,
            #cierre         = hora_cierre,
        )
        e.save()
        return e

    # TDD
    def test_primera_vista_disponible(self):
        response = self.client.get('/estacionamientos/')
        self.assertEqual(response.status_code, 200)
        
    # malicia 
    def test_llamada_a_la_raiz_lleva_a_estacionamientos(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)
        
    # integracion TDD
    def test_llamada_a_los_detalles_de_un_estacionamiento(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle-estacionamiento.html')
    
    # integracion malicia
    def test_llamada_a_los_detalles_sin_estacionamiento_creado(self):
        response = self.client.get('/estacionamientos/1/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
    
    # integracion TDD
    def test_llamada_a_reserva(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 200)
        
    # integracion malicia 
    def test_llamada_a_reserva_sin_estacionamiento_creado(self):
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        
    # integracion malicia
    def test_llamada_a_tasa_sin_parametros_especificados_aun(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/tasa')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'template-mensaje.html')
        
    # integracion esquina
    def test_llamada_a_la_generacion_de_grafica_empty_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/grafica/')
        self.assertEqual(response.status_code, 400)
        
    # integracion TDD
    def test_llamada_a_la_generacion_de_grafica_normal_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/grafica/?2015-03-10=10.5')
        self.assertEqual(response.status_code, 200)
    
    # integracion malicia
    def test_llamada_a_la_generacion_de_grafica_bad_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/grafica/?hola=chao')
        self.assertEqual(response.status_code, 400)
    
    # integracion malicia
    def test_llamada_a_la_reserva_por_sms_bad_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/sms?phone=04242221111&text=hola')
        self.assertEqual(response.status_code, 400)
       
    # integracion esquina
    def test_llamada_a_la_reserva_por_sms_empty_request(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/sms')
        self.assertEqual(response.status_code, 400)
        
    # integracion esquina
    def test_llamada_a_reserva_sin_parametros_especificados_aun(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 403)
    
    # integracion TDD
    def test_llamada_a_consultar_reserva(self):
        response = self.client.get('/estacionamientos/consulta_reserva')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar-reservas.html')
    
    # integracion TDD 
    def test_llamada_a_consultar_ingreso(self):
        response = self.client.get('/estacionamientos/ingreso')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar-ingreso.html')
    
    # integracion malicia  
    def test_llamada_a_url_inexistente(self):
        response = self.client.get('/este/url/no/existe')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
    
    # integracion TDD
    def test_llamada_a_pago_get(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.get('/estacionamientos/1/pago')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pago.html')
    
    # integracion TDD  
    def test_llamada_a_pago_post(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.post('/estacionamientos/1/pago')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pago.html')
    
    # integracion malicia
    def test_llamada_a_pago_sin_parametros_especificados_aun(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/reserva')
        self.assertEqual(response.status_code, 403)
    
    # integracion malicia
    def test_llamada_a_pago_sin_estacionamiento_creado(self):
        response = self.client.get('/estacionamientos/1/pago')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    # Borde
    def test_vista_propietarios(self):
        response = self.client.get('/estacionamientos/propietarios')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo-propietarios.html')
        
    # Borde
    def test_vista_billetera_electronica(self):
        response = self.client.get('/estacionamientos/billetera_electronica')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Billetera-Electronica.html')

    # Borde
    def test_vista_billetera_electronica_recargar(self):
        response = self.client.get('/estacionamientos/billetera_electronica/recargar')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'billetera_electronica_recarga.html')
    
    # Borde
    def test_vista_crear_billetera_electronica(self):
        response = self.client.get('/estacionamientos/billetera_electronica/crear')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'billetera_electronica_crear.html')

    # Borde
    def test_vista_pagar_con_billetera_electronica(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.get('/estacionamientos/1/pago_billetera')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pago_billetera.html')
    
    # Borde
    def test_vista_cancelar_reserva(self):
        response = self.client.get('/estacionamientos/cancelar_reserva')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelar.html')
        
    # Borde
    def test_vista_cambiar_pin(self):
        response = self.client.get('/estacionamientos/billetera_electronica/cambiar_pin')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'billetera_electronica_cambiar_pin.html')
     
    # Borde   
    def test_llamada_a_cambiar_propietario_sin_hora_apertura(self):
        self.crear_estacionamiento(1)
        response = self.client.get('/estacionamientos/1/cambiar_propietario')
        self.assertEqual(response.status_code, 403)
        
    # Borde   
    def test_llamada_a_cambiar_propietario(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.get('/estacionamientos/1/cambiar_propietario')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cambiar-propietario.html')
        
    # Borde
    def test_vista_mover_reserva(self):
        response = self.client.get('/estacionamientos/moverReserva')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mover.html')
    
    # Borde
    def test_vista_mover_reserva_horario(self):
        response = self.client.get('/estacionamientos/moverReservaHorario')
        self.assertEqual(response.status_code, 301)
        
########################################################################
#                        POST
########################################################################

    # Borde
    def test_vista_propietarios_post(self):
        response = self.client.post('/estacionamientos/propietarios',{'nombre':'Juana','ci':'V-12345679','tel':'0412-1238567'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo-propietarios.html')
    
    # Borde
    def test_primera_vista_disponible_post(self):
        response = self.client.post('/estacionamientos/',{'ci_propietario':'V-12345679','nombre':'23 de Junio','direccion':'Baralt,','rif':'J-123456789'})
        self.assertEqual(response.status_code, 200)
    
    # Borde
    def test_llamada_a_consultar_ingreso_post(self):
        response = self.client.post('/estacionamientos/ingreso',{'rif':'J-123456789'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar-ingreso.html')
    
    # Borde    
    def test_llamada_a_consultar_reserva_post(self):
        response = self.client.post('/estacionamientos/consulta_reserva',{'ci':'V-12345679'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar-reservas.html')
        
    # Borde
    def test_vista_cancelar_reserva_post(self):
        response = self.client.post('/estacionamientos/cancelar_reserva',{'ci':'V-12345679','idReserva':'1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelar.html')
    
    # Borde    
    def test_vista_billetera_electronica_post(self):
        response = self.client.post('/estacionamientos/billetera_electronica',{'idValid':'0','pinValid':'0000'})
        self.assertEqual(response.status_code, 200)
        ##self.assertTemplateUsed(response, 'Billetera-Electronica.html')
        
    # Borde
    def test_vista_crear_billetera_electronica_post(self):
        response = self.client.post('/estacionamientos/billetera_electronica/crear',{'nombreUsu':'Andres','apellidoUsu':'Rey','ciUsu':'V-12345678','pinUsu':'0001'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'billetera_electronica_crear.html')
        
    # Borde
    def test_vista_billetera_electronica_recargar_post(self):
        response = self.client.post('/estacionamientos/billetera_electronica/recargar',{'idBill':'0','monto':'2000','pinValid':'0001'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'billetera_electronica_recarga.html')
        
    # Borde
    def test_vista_cambiar_pin_post(self):
        response = self.client.post('/estacionamientos/billetera_electronica/cambiar_pin',{'idBill':'0','pinUsu':'0001','nuevo_pin':'0002','confirmar_pin':'0002'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'template-mensaje.html')
    
    # Borde    
    def test_llamada_a_los_detalles_de_un_estacionamiento_post(self):
        self.crear_estacionamiento(1)
        response = self.client.post('/estacionamientos/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle-estacionamiento.html')
    
    # Borde    
    def test_llamada_a_editar_dias_feriados_de_un_estacionamiento_post(self):
        self.crear_estacionamiento(1)
        response = self.client.post('/estacionamientos/1/feriados',{'dia':'2016-06-15','descripcion':'prueba'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dias_feriados.html')    
    
    # Borde
    def test_llamada_a_cambiar_propietario_post(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.post('/estacionamientos/1/cambiar_propietario',{'ci_propietario':'V-12345677'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cambiar-propietario.html')
    
    # Borde    
    def test_llamada_a_reserva_post(self):
        pro = Propietario(
            nombre = "Juana",
            ci = 'V-12345679',
            tel = "0412-1238567"
        )
        pro.save()
        e = Estacionamiento(
            ci_propietario = pro,
            nombre = "nom",
            direccion = "dir",
            rif = "rif",
            capacidad = 20,
            apertura = time(0,0),
            cierre = time(23,59),
        )
        e.save()
        response = self.client.post('/estacionamientos/1/reserva',{'nombre':'Carlos','direccion':'Caracas'})
        self.assertEqual(response.status_code, 200)
        
    # Borde
    def test_vista_mover_reserva_post(self):
        response = self.client.post('/estacionamientos/moverReserva')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mover.html')
    
    # Borde
    def test_vista_mover_reserva_horario_post(self):
        response = self.client.post('/estacionamientos/moverReservaHorario')
        self.assertEqual(response.status_code, 301)