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