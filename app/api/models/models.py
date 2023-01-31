from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    identificacion = Column(String)

class Ausencia(Base):
    __tablename__ = 'ausencia'
    id = Column(Integer, primary_key=True)
    alumno_id = Column(Integer)
    motivo = Column(String)
    tiempo = Column(String)
