# TODOS Django Elektron:

## Inicio / Settings.py:
	- Cuando se arranca el server debe arrancar mqtt y websocket (una sola instancia de c/u)
	- Se deben crear TaskStates, TaskFunctions y DeviceState por defecto al iniciar el sistema. Ver cuales. 


## Model:
	- Ver como solucionar la url, la view y la template para listar data y task de un device elegido por la url 
	- Crear las vistas (Alta, Baja, Modificación y Listar) y las urls de cada modelo.
	- Listar: Lograr urls para cada modelo para obtener todos los datos en formato json.
	- Alta, Baja Moficicación: Lograr post y get para crear, editar y borrar datos para cada modelo.
	- Lograr todo lo anterior pero con authenticación.

## Login:
	- Hacer el login y authenticación.


## MQTT:
	- Falta la vuelta desde el server a mqtt
	- Ver seguridad MD5 salt en nodemcu y en el server.

## Websocket:
	- Ver como integrar websocket para enviar los datos de un device en tiempo real.
	- Lo mismo pero con muchos devices.
	- Ver seguridad.
