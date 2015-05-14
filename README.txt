Cambios realizados:
    
 1.-Se crea el modelo propietario en estacionamientos/models.py
 2.-Se crea la forma en base al modelo propietario en estacionamientos/forms.py
 3.-Se agrega el modelo propietario a admin.py para que se creara su tabla en la base de datos
 4.-Se extendio la vista estacionamientos_all en estacionamientos/views.py para que desplegara y recibiera el formulario de propietario
 5.-Se modifica el template catalogo-estacionamientos.html para que mostrara propietario.
 6.-Se crea las pruebas de form de propietarios.
 7.-Arreglado el html, muestra todo con buen formato ahora.
    
Por hacer:

    1.-Hacer de propietario en estacionamiento una clave foranea a Propietario
    2.-Que no de error por dejar campos del otro formulario vacio