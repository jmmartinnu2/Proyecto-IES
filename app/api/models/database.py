import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Proyecto_IES.models import Base

# Crea un motor de base de datos a partir de la ruta a nuestra base de datos SQLite
engine = create_engine('sqlite:///datos.db', echo=True)

# Crea todas las tablas especificadas en nuestros modelos
Base.metadata.create_all(engine)

# Crea una sesión de la base de datos
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    # Inicializa la base de datos
    Base.metadata.create_all(engine)

def add_alumno(nombre, apellido, identificacion):
    # Agrega un alumno a la base de datos
    alumno = Alumno(nombre=nombre, apellido=apellido, identificacion=identificacion)
    session.add(alumno)
    session.commit()

def add_ausencia(alumno_id, motivo, tiempo):
    # Agrega una ausencia a la base de datos
    ausencia = Ausencia(alumno_id=alumno_id, motivo=motivo, tiempo=tiempo)
    session.add(ausencia)
    session.commit()

def get_alumno(identificacion):
    # Obtiene un alumno a partir de su identificación
    alumno = session.query(Alumno).filter_by(identificacion=identificacion).first()
