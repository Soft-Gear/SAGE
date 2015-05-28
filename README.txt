Resolución de conflictos Casos de prueba:

Cambios realizados en test_estacionamiento_form:
    
 1.-Se modifican los registros de data form cuyo parametro es 'propietario' por 'ci_propietario' en todas la pruebas. 
 2.-Se agregan casos faltantes debido a la modificacion:
 
 	1. test_ciPropietario_invalido_cinco_digitos
 	2. test_ciPropietario_valido_seis_digitos
 	3. test_ciPropietario_formato_invalido
 	4. test_ciPropietario_invalido_formato_string
 	5. test_nombreEstacionamiento_valido_simbolos

Cambios realizados en tests_propietario_form:

-Se agregan casos faltantes debido a la modificaion:
 
 	1. test_nombre_valido_dieresis_acento
 	2. test_nombre_valido_guion_comilla
 	
Cambios realizados en tests_consulta_reserva:

-Se crea un objeto propietario para la base de datos temporal para el desarrollo y acoplamiento de las siguientes pruebas:
   
	1. test_dos_estacionamientos_muchos_pagos
	2. test_estacionamiento_sin_pagos
	3. test_muchos_estacionamiento_con_disintos_rif
	4. test_muchos_estacionamiento_mitad_sin_pagos
	5. test_muchos_estacionamiento_sin_pagos
	6. test_un_estacionamiento_muchos_pagos
	7. test_un_estacionamiento_un_pago

Cambios realizados en tests_integration:

-Se crea un objeto propietario para la base de datos temporal en el metodo crear_estacionamiento, el cual soluciona:

	1. test_llamada_a_la_generacion_de_grafica_bad_request
	2. test_llamada_a_la_generacion_de_grafica_empty_request
	3. test_llamada_a_la_generacion_de_grafica_normal_request
	4. test_llamada_a_la_reserva_por_sms_bad_request
	5. test_llamada_a_la_reserva_por_sms_empty_request
	6. test_llamada_a_los_detalles_de_un_estacionamiento
	7. test_llamada_a_pago_sin_parametros_especificados_aun
	8. test_llamada_a_reserva_sin_parametros_especificados_aun
	9. test_llamada_a_tasa_sin_parametros_especificados_aun

FAILED (failures=5, errors=41)

-Se crea un objeto propietario para la base de datos temporal para el desarrollo y acoplamiento de las siguientes pruebas:

	1. test_llamada_a_pago_get
	2. test_llamada_a_pago_post
	3. test_llamada_a_reserva

FAILED (failures=5, errors=38)

Cambios realizados en tests_marzullo:

-Se crea un objeto propietario para la base de datos temporal en el metodo crear_estacionamiento, el cual soluciona:

1. testAddThreeReservations
2. testAddTwoReservation
3. testAddTwoReservation2
4. testAllSmallestReservations
5. testFiveSpotsFiveReservation
6. testFiveSpotsSixReservation
7. testFiveSpotsSixReservationNoOverlapping
8. testFullPlusOne
9. testManyReservationsMaxOverlapping
10. testManyReservationsOneOverlap
11. testNoSpotParking
12. testOneReservationEarly
13. testOneReservationFullDay
14. testOneReservationLate
15. testOneReservationMax
16. testSmallestReservation
17. testTenSpotsOneReservation

FAILED (failures=5, errors=21)

Cambios realizados en tests_tasa_reservacion:

-Se crea un objeto propietario para la base de datos temporal en el metodo crear_estacionamiento, el cual soluciona:

1. test_dos_reservaciones_mismo_dia
2. test_estacionamiento_horario_restringido_mitad_capacidad_primer_dia
3. test_estacionamiento_horario_restringido_toda_capacidad_primer_dia
4. test_estacionamiento_reserva_siete_dias
5. test_estacionamiento_reserva_siete_dias_antes_media_noche
6. test_estacionamiento_reserva_un_dia_dos_casillas
7. test_estacionamiento_reserva_un_dia_mas_un_minuto
8. test_estacionamiento_reserva_un_dia_sola_casilla
9. test_estacionamiento_reserva_un_dia_sola_casilla_menos_un_minuto
10. test_estacionamiento_reserva_una_hora_cambio_fecha_mediaNoche
11. test_estacionamiento_reserva_una_hora_dos_puestos
12. test_estacionamiento_reserva_una_hora_sin_cambio_fecha
13. test_estacionamiento_siempre_abierto_mitad_capacidad_primer_dia
14. test_estacionamiento_sin_reservas
15. test_estacionamiento_vacio
16. test_horario_restringido_toda_capacidad_primer_dia_exceso_1_minuto
17. test_horario_restringido_toda_capacidad_primer_dia_y_un_minuto
18. test_reserva_6_dias_misma_hora
19. test_reserva_inicio_antes_de_inicioVentana_fin_despues_inicioVentana
20. test_reservaciones_de_una_hora_24_horas
21. test_reservaciones_de_una_hora_6_a_18_horas

FAILED (failures=5)
