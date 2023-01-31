# Aplicación para Control de Ausencias en el Aula

## Introducción
Esta aplicación móvil permite a los profesores registrar las ausencias de los alumnos en tiempo real durante las clases. El objetivo es tener un registro de los alumnos que se ausentan de la clase durante su transcurso. El profesor puede buscar la identificación del alumno, seleccionar el motivo de la ausencia de una lista de opciones predefinidas, y confirmar la ausencia activando un botón. Un contador de tiempo controla la duración de la ausencia y se envía en tiempo real a una aplicación web monitoreada por el jefe de estudios. Si el alumno supera el tiempo establecido para la ausencia, se activará una alerta.

## Funcionamiento Básico
1. El profesor accede a la aplicación móvil y busca la identificación del alumno.
2. Selecciona el motivo de la ausencia del alumno de una lista de opciones predefinidas.
3. Confirma la ausencia activando el botón correspondiente.
4. Se activa un contador de tiempo para controlar la ausencia.
5. Si el alumno supera el tiempo establecido para la ausencia, se activará una alerta.

## Tecnologías Utilizadas
- Lenguaje de programación: Python
- Framework de Backend: FastAPI
- Base de datos: SQLite3

## Instalación de Librerias
pip install -r requirements.txt


## Inicio del Proyecto
python app/main.py


## Estructura de Archivos
Proyecto-IES/
|-- app/
| |-- init.py
| |-- api/
| | |-- init.py
| | |-- routers/
| | | |-- init.py
| | | |-- routes.py
| | |-- models/
| | | |-- init.py
| | | |-- database.py
| | | |-- models.py
| |-- main.py
|-- .env
|-- .gitignore
|-- requirements.txt
|-- setup.py


## Aspectos técnicos para la implementación del proyecto
1. Análisis de requisitos: define claramente los requisitos de la aplicación, incluyendo los motivos de ausencia, el contador de tiempo, la notificación, la aplicación web, la alarma emergente y el control de registro.

2. Diseño de la base de datos: determine las tablas y campos necesarios para almacenar la información, como el nombre y ID del alumno, el motivo de la ausencia y el tiempo de ausencia.

3. Desarrollo de la aplicación móvil: utilice Python y un marco de desarrollo móvil compatible, como Kivy, para desarrollar la aplicación móvil. La aplicación debe permitir a los profesores activar la notificación de ausencia y seleccionar el motivo de la ausencia.

4. Desarrollo de la aplicación web: utilice FastAPI y un framework frontend compatible, como React, para desarrollar la aplicación web. La aplicación web debe permitir monitorear en tiempo real la información de ausencia y el contador de tiempo.

5. Integración de la base de datos: conecte la base de datos SQLite3 a las aplicaciones móvil y web para almacenar y recuperar la información de ausencia.

6. Implementación de la alarma emergente: utilice la función de temporizador de Python para implementar la alarma emergente que se activará si el tiempo de ausencia supera un límite establecido.

7. Pruebas: realice pruebas exhaustivas de las aplicaciones móvil y web para asegurarse de que cumplen con los requisitos y funcionan correctamente.

8. Implementación del servidor: utilize Uvicorn como servidor para ejecutar la aplicación web y asegurarse de que esté disponible para los usuarios.



## Diseñamos la base de datos
Para diseñar la base de datos, primero debemos identificar las entidades o tablas que se requieren para almacenar la información y las relaciones entre ellas.

Podríamos tener una tabla "Alumno" que contenga información sobre los alumnos, como su nombre, apellido, identificación, etc.

Luego tendríamos una tabla "Clase" que contenga información sobre las clases, como el nombre de la clase, el profesor, la fecha, etc.

También tendríamos una tabla "Ausencia" que registre las ausencias de los alumnos durante las clases. Esta tabla debería tener una relación con la tabla "Alumno" y la tabla "Clase". Además, también podríamos agregar una columna para el motivo de la ausencia.

Por último, podríamos tener una tabla "Alerta" que registre las alertas activadas si un alumno supera el tiempo establecido para la ausencia. Esta tabla debería tener una relación con la tabla "Ausencia".