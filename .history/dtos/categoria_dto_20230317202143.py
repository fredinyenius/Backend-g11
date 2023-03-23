from marshmallow_sqlalchemy import SQLAlchemyAutoSchema,auto_field
from models.categoria_model import Usuario

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario