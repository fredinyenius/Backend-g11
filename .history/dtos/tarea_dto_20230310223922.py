from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
#from marshmallow import Schema, fields
from models.tarea_model import Tarea

class TareaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea