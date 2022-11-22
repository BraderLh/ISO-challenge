# Reto de Python - ISO

## Generación de datos
Primero se ha creado un código fuente albergado en el archivo ***save-data.py***, el cual genera un archivo tipo *json* con los datos iniciales detallados en el mismo documento del reto técnico. Por lo que genera un archivo con el nombre de -> **data.json**.

## Obtención y manejo de datos
Se ha definido una serie de funciones las cuales son especificas también por el mismo documento, las cuales son:

* Agregar
* Eliminar
* Actualizar
* Salir

Se ha agregado la función de *"Mostrar"*, el cual se encarga de mostrar el formato deseado en pantalla/consola como se solicita el documento. Por otro lado, para demostrar que cada una de las funciones realiza una ejecución correcta se ha configurado archivos de salida distintos para cada función que modifica el archivo original de datos. 

No obstante, este puede cambiarse y probarse con el archivo original, es decir, podemos utilizar *data.json* reemplazando los nombres de salida estableciod en cada una de las funciones por el nombre de `json_files[0]` sin ningún problema. Sólo se hizo este cambio para demostrar y comprobar los cambios hechos en el conjunto de datos inicial. 

## Menu
Finalmente se desarrolló un menu de opciones los cuales simulan una interfaz de usuario. Todo esto, es llamado en la función *main.py*
