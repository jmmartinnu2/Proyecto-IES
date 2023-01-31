from fastapi import FastAPI, Depends
from .models import Alumno, Ausencia
from .database import session, add_alumno, add_ausencia, get_alumno

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/alumno")
def add_alumno(nombre: str, apellido: str, identificacion: str):
    add_alumno(nombre, apellido, identificacion)
    return {"message": "Alumno añadido exitosamente"}

@app.post("/ausencia")
def add_ausencia(alumno_id: int, motivo: str, tiempo: str):
    add_ausencia(alumno_id, motivo, tiempo)
    return {"message": "Ausencia añadida exitosamente"}

@app.get("/alumno/{identificacion}")
def get_alumno(identificacion: str):
    alumno = get_alumno(identificacion)
    if alumno is None:
        return {"error": "Alumno no encontrado"}
    return {"nombre": alumno.nombre, "apellido": alumno.apellido, "identificacion": alumno.identificacion}

@app.post("/alumno/{identificacion}/ausencia")
def add_ausencia_for_alumno(identificacion: str, motivo: str, tiempo: str):
    alumno = get_alumno(identificacion)
    if alumno is None:
        return {"error": "Alumno no encontrado"}
    add_ausencia(alumno.id, motivo, tiempo)
    return {"message": "Ausencia añadida exitosamente"}

@app.get("/alumno/{identificacion}/ausencias")
def get_ausencias_for_alumno(identificacion: str):
    alumno = get_alumno(identificacion)
    if alumno is None:
        return {"error": "Alumno no encontrado"}
    ausencias = [{"motivo": a.motivo, "tiempo": a.tiempo} for a in alumno.ausencias]
    return {"ausencias": ausencias}
