from bd import conexion
from sqlalchemy import Column, types

class Usuario(conexion.Model):
    id = Column(types_=types.Integer, autoincrement=True, primary_key=True)
    correo = Column(types_=types.Integer, unique=True, nullable=False)
    password = Column(types_=types.Integer, nullable=False)
    nombre = Column(types_=types.Integer, nullable=False)
    apellido = Column(types_=types.Integer, nullable=False)

    __tablename__ = 'usuarios'