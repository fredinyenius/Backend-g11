from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.tarea_model import Tarea

class TareaDto(SQLAlchemyAutoSchema):
 
    class Meta:
        model = Tarea

class EstadoTareaEnum():
    PENDIENTE = 'PENDIENTE'
    REALIZANDOSE = 'REALIZANDOSE'
    REALIZADA = 'REALIZADA'
    CANCELADA = 'CANCELADA'