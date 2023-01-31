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


