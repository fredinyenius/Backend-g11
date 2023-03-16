from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from models.tarea_model import Tarea

class TareaDto(SQLAlchemyAutoSchema):
    password = auto_field(load_only=True)
    class Meta:
        model = Tarea

   