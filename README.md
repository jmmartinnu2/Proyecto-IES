#Aplicación para Control de Ausencias en el Aula

Introducción
Esta aplicación móvil permite a los profesores registrar las ausencias de los alumnos en tiempo real durante las clases. El propósito de la aplicación es tener un registro de los alumnos que se ausentan de la clase en mitad de la misma. Por ejemplo, están en una clase con su profesor y el alumno Juan quiere ir al baño, pues su profesor accede a la aplicación móvil, busca la identificación del alumno por su ID, nombre o lo que sea y activa su botón de ausencia, confirmando el tipo de ausencia que será un select con diferentes motivos: pueden ser: ausencia para ir al baño, ausencia para hablar con la orientadora, ausencia por encontrarse indispuesto, ausencia por visita médica, entre otros.

#Funcionamiento Básico
El profesor accede a la aplicación móvil y busca la identificación del alumno que se ausentará de la clase.
Selecciona el motivo de la ausencia del alumno de una lista de opciones predefinidas.
Confirma la ausencia activando el botón correspondiente.
Se activa un contador de tiempo para controlar esa ausencia, el cual se enviará en tiempo real a una aplicación web monitoreada por el jefe de estudios desde su sala.
Si el alumno ausentado pasa el tiempo estipulado y configurado para la ausencia, se activará una alerta o notificación para tomar medidas contra él, ya que ha sobrepasado el tiempo establecido.


#Tecnologías Utilizadas
Lenguaje de programación: Python
Framework de Backend: FastAPI
Base de datos: SQLite3



#Estructura de Archivos
Proyecto-IES/
|-- app/
|   |-- __init__.py
|   |-- api/
|   |   |-- __init__.py
|   |   |-- routers/
|   |   |   |-- __init__.py
|   |   |   |-- routes.py
|   |   |-- models/
|   |   |   |-- __init__.py
|   |   |   |-- database.py
|   |   |   |-- models.py
|   |-- main.py
|-- .env
|-- .gitignore
|-- requirements.txt
|-- setup.py


Instalación de Librerias
Para instalar todas las librerías necesarias para el proyecto, se puede utilizar el siguiente comando en la línea de comandos:
pip install -r requirements.txt


Inicio del Proyecto
Para iniciar el proyecto, se debe ejecutar el siguiente comando en la línea de comandos:
python app/main.py


Estructura del Proyecto
La estructura del proyecto está organizada de la siguiente manera:
Proyecto-IES/
|-- app/
|   |-- __init__.py
|   |-- api/
|   |   |-- __init__.py
|   |   |-- routers/
|   |   |   |-- __init__.py
|   |   |   |-- routes.py
|   |   |-- models/
|   |   |   |-- __init__.py
|   |   |   |-- database.py
|   |   |   |-- models.py
|   |-- main.py
|-- .env
|-- .gitignore
|-- requirements.txt
|-- setup.py



Tecnologías utilizadas
Python 3.8
FastAPI
SQLite3

Propósito de la App
El propósito de la aplicación móvil es tener un registro de los alumnos que se ausentan de clase en medio de la clase. Por ejemplo, si un alumno quiere ir al baño durante una clase, su profesor puede acceder a la aplicación móvil, buscar la identificación del alumno por su ID, nombre, u otro dato, y activar su botón de ausencia. El profesor también puede confirmar el tipo de ausencia que será un select con diferentes motivos: pueden ser ausencia para ir al baño, ausencia para hablar con la orientadora, ausencia por encontrarse indispuesto, o ausencia por visita médica, entre otros.

En cuanto el alumno se ausenta, el profesor activa la alerta y se activa un contador de tiempo para controlar esa ausencia, que automáticamente y en tiempo real se envía a una aplicación web que está monitoreada por el jefe de estudios desde su sala. Si el alumno ausentado pasa el tiempo estipulado y configurado para la ausencia que haya realizado, se activa una alerta o notificación para tomar medidas contra ese alumno, entendiendo que ya ha sobrepasado el tiempo estipulado.

Este sería un funcionamiento básico de la aplicación, y solo los profesores tendrán acceso a ella.