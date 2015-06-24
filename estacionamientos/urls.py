# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from estacionamientos import views


# Este error es raro, en django funciona
urlpatterns = patterns('',
    url(r'^$', views.estacionamientos_all, name = 'estacionamientos_all'),
    url(r'^(?P<_id>\d+)/$', views.estacionamiento_detail, name = 'estacionamiento_detail'),
    url(r'^(?P<_id>\d+)/reserva$', views.estacionamiento_reserva, name = 'estacionamiento_reserva'),
    url(r'^moverReserva$', views.estacionamiento_moverReserva, name = 'estacionamiento_moverReserva'),
    url(r'^moverReservaMoverRecargar$', views.estacionamiento_RecargarBilleteraMover, name = 'estacionamiento_RecargaBilleteraMover'),
    url(r'^moverReservaHorario/(?P<_idres>\d+)$', views.estacionamiento_moverReservaHorario, name = 'estacionamiento_moverReservaHorario'),
    url(r'^(?P<_id>\d+)/feriados$', views.estacionamiento_feriados, name = 'estacionamiento_feriados'),  
    url(r'^(?P<_id>\d+)/feriados/remover$', views.estacionamiento_feriados_remover, name = 'estacionamiento_feriados_remover'), 
    url(r'^(?P<_id>\d+)/feriados/remover/(?P<_idrem>\d+)$', views.estacionamiento_feriados_remover, name = 'estacionamiento_feriados_remover'), 
    url(r'^cancelar_reserva$', views.estacionamiento_cancelar_reserva, name = 'estacionamiento_cancelar_reserva'),
    url(r'^cancelar_reserva/billetera$', views.estacionamiento_cancelar_reserva_billetera, name = 'estacionamiento_cancelar_reserva_billetera'),
    url(r'^(?P<_id>\d+)/cambiar_propietario$', views.cambiar_propietario, name = 'cambiar_propietario'),
    url(r'^(?P<_id>\d+)/pago$', views.estacionamiento_pago, name = 'estacionamiento_pago'),
    url(r'^(?P<_id>\d+)/pago/(?P<_idres>\d+)$', views.estacionamiento_pago, name = 'estacionamiento_pago'),
    url(r'^(?P<_id>\d+)/pago_billetera$', views.estacionamiento_pago_billetera, name = 'estacionamiento_pago_billetera'),
    url(r'^(?P<_id>\d+)/pago_billetera/(?P<_idres>\d+)$', views.estacionamiento_pago_billetera, name = 'estacionamiento_pago_billetera'),
    url(r'^ingreso$', views.estacionamiento_ingreso, name = 'estacionamiento_ingreso'),
    url(r'^consulta_reserva$', views.estacionamiento_consulta_reserva, name = 'estacionamiento_consulta_reserva'),
    url(r'^billetera_electronica$', views.billetera_electronica, name = 'billetera_electronica'),
    url(r'^billetera_electronica/$', views.billetera_electronica_crear, name = 'billetera_electronica_crear'),
    url(r'^billetera_electronica/crear$', views.billetera_electronica_crear, name = 'billetera_electronica_crear'),
    url(r'^billetera_electronica/recargar$', views.billetera_electronica_recargar, name = 'billetera_electronica_recargar'),
    url(r'^sms$', views.receive_sms, name='receive_sms'),
    url(r'^(?P<_id>\d+)/tasa$', views.tasa_de_reservacion, name = 'tasa_de_reservacion'),
    url(r'^grafica/.*$', views.grafica_tasa_de_reservacion, name = 'grafica_tasa_de_reservacion'),
    url(r'^propietarios$', views.propietarios_all, name = 'propietarios_all')
)
