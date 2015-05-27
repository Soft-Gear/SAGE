Cambios realizados para historia 1:
    
 1.-Se crea el modelo propietario en estacionamientos/models.py
 2.-Se crea la forma en base al modelo propietario en estacionamientos/forms.py
 3.-Se agrega el modelo propietario a admin.py para que se creara su tabla en la base de datos
 4.-Se extendio la vista estacionamientos_all en estacionamientos/views.py para que desplegara y recibiera el formulario de propietario
 5.-Se modifica el template catalogo-estacionamientos.html para que mostrara propietario.
 6.-Se crea las pruebas de form de propietarios.
 7.-Arreglado el html, muestra todo con buen formato ahora.
    
Faltante de historia 1:

1. Capacidad de editar propietarios de estacionamiento.
    
Cambios realizados para historia 2:

1.-Se crea el modelo BilleteraElectronica en estacionamientos/models.py 
2.-Se crea la forma en base al modelo BilleteraElectronica en estacionamientos/forms.py
3.-Se crea la base de datos de BilleteraElectronica en estacionamientos/admin.py 
4.-Se agrego la vista BilleteraElectronica en estacionamientos/views.py para generar el url deseado 
5.-Se agrega el template billetera-electronica.html que por ahora no hace nada
6.-Se agrega un nuevo url en estacionemientos/url.py para manejar la nueva vista

Faltante de historia 2:

1.-Registrar los pagos en la base de datos
2.-Pruebas correspondientes a BilleteraElectronica