from bd import conexion
from sqlalchemy import Column, types

class Usuario(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    correo = Column(type_=types.Integer, unique=True, nullable=False)
    password = Column(type_=types.Integer, nullable=False)
    nombre = Column(type_=types.Integer, nullable=False)
    apellido = Column(type_=types.Integer, nullable=False)

    __tablename__ = 'usuarios'