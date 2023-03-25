from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)

    class Meta:
        # sirve para modificar alguna configuracion de la tabla de nuestro bd
        db_table = 'categorias'


class Producto(models.Model):
    nombre = models.TextField(null=False)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)

#en la base de datos se llama snike case y en el API su formato es camelcase
#createdAt es el campo que automaticament registrara la hora y fecha del servidor cuando se cree un nuevo registro
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    #UpdatedAt es el campo que se actualizará cada vez que modifiquemos algun dato del registro con la fecha actual
    updatedAt = models.DateTimeField(auto_now=True, db_column='update_at')

    #relaciones
    # on_delete > es la accion que tomara al momento de hacer la eliminacion de una categoria y si esta tiene productos
    # CASCADE > elimina la categoria y luego elimina en forma consecutiva a todos los productos de esa categoria
    # PROTECT > evita la eliminacion de la categoria siempre y cuando esta tenga productos y lanzara un error de tipo IntegrityError
    # RESTICT > evita la eliminacion al igual que el PROTECT pero esto emitira un error de tipo RestrictedError
    # SET_NULL > elimina la categoria y a todos sus productos les cambia el valor de la categoria_id a NULL
    # SET_DEFAULT > elimina la categoria y de acuerdo al valor que le colocamos en default lo cambiara a ese valor
    # DO_NOTHING > No realiza ninguna accion, elimina la categoria y no hace ningun cambio en los productos, No se debe utilizar esta opcion ya que genera mala integridad de los datos
    Categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE, db_column='categoria_id',
                                  related_name='productos')
    
    class Meta:
        db_table = 'productos'


