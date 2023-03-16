from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from enum import Enum
from models.tarea_model import Tarea

class TareaDto(SQLAlchemyAutoSchema):
 
    class Meta:
        model = Tarea

class EstadoTareaEnum(Enum):
    PENDIENTE = 'PENDIENTE'
    REALIZANDOSE = 'REALIZANDOSE'
    REALIZADA = 'REALIZADA'
    CANCELADA = 'CANCELADA'