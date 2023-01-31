from fastapi import FastAPI
from Proyecto_IES.database import engine, Base, Session, add_alumno, get_alumno


app = FastAPI()

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    # Cierra la sesión de la base de datos
    session.close()

@app.post("/alumno")
async def create_alumno(nombre: str, apellido: str, identificacion: str):
    # Agrega un alumno a la base de datos
    add_alumno(nombre, apellido, identificacion)
    return {"message": "Alumno creado"}

@app.get("/alumno/{identificacion}")
async def read_alumno(identificacion: str):
    # Obtiene un alumno a partir de su identificación
    alumno = get_alumno(identificacion)
    return {"nombre": alumno.nombre, "apellido": alumno.apellido, "identificacion": alumno.identificacion}
