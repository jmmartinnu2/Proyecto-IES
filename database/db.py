from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    username = Column(String)
    password = Column(String)
    tipo_salida = Column(String)
    tiempo_salida = Column(String)

engine = create_engine('sqlite:///alumnos.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Agrega un registro para cada alumno
alumno1 = Alumno(nombre='Juan', apellido='Perez', username='jperez', password='1234', tipo_salida='permiso', tiempo_salida='10:00am')
alumno2 = Alumno(nombre='Maria', apellido='Gonzalez', username='mgonzalez', password='5678', tipo_salida='permiso', tiempo_salida='11:00am')

session.add(alumno1)
session.add(alumno2)

session.commit()
session.close()
