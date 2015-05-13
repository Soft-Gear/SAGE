Cambios realizados:
    
 1.-se creó el modelo propietario en estacionamientos/models.py
 2.-se creó la forma en base al modelo propietario en estacionamientos/forms.py
 3.-se agregó el modelo propietario a admin.py para que se creara su tabla en 
       la base de datos
 4.-Se extendió la vista estacionamientos_all en estacionamientos/views.py para
    que desplegara y recibiera el formulario de propietario
 5.-Se modificó el template catalogo-estacionamientos.html para que mostrara 
    propietario
    
Por hacer:

    1.-Hacer de propietario en estacionamiento una clave foranea a Propietario
    2.-Mover el formulario de propietario a la derecha
    3.-Que no de error por dejar campos del otro formulario vacio
