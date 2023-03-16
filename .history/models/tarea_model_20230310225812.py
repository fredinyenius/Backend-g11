from bd import conexion
from enum import Enum
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, types



class EstadoTareaEnum(Enum):
    PENDIENTE = 'PENDIENTE'
    REALIZANDOSE = 'REALIZANDOSE'
    REALIZADA = 'REALIZADA'
    CANCELADA = 'CANCELADA'

class Tarea(conexion.Model):
    id = Column(types_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(types_=types.Text, nullable=False)
    descripcion = Column(types_=types.Text, default='No tiene descripcion')
    fecha_vencimiento = Column(types_=types.DateTime, name='fecha_vencimiento')
    estado = Column(types_=types.Enum(EstadoTareaEnum), default=EstadoTareaEnum.PENDIENTE)
    
    
    usuarioId = Column(ForeignKey(column='usuarios.id'), types_=types.Integer, nullable=False)

    __tablename__ = 'usuarios'