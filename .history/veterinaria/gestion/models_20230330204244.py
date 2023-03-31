from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ManejoUsuario(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, password, tipoUsuario):
        
        if not correo :
            raise ValueError('El usuario de tener un correo')
        
        #normalize_email > sirve para llevar todo el crreo a minisculas y ademas le quita 
        # espacios en blancos i verifica si los caracteres son validos
        
        correo_normalizado = self.normalize_email(correo)

        nuevo_usuario = self.model(correo = correo_normalizado, nombre = nombre, apellido = apellido,
                                   tipoUsuario = tipoUsuario)
        
        # generamos el hash de nuestro password
        nuevo_usuario.set_password(password)
        #is_superuser > indica que el usuario tiene la totalidad de priviligegios para hacedr loque desee en l panel administrativo

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)

    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False) 
    password = models.TextField(null=False) 
    # CharFiel > varchar ( limite)
    #TextField > LIMITE no es necesario a nivel de base de datos
    tipoUsuario = models.CharField(max_length=100, choices=[('ADMIN','ADMIN'),('CLIENTE','CLIENTE')],
    db_column='tipo_usuario')

    # campos netamente de auth_user
    # is_staff > sirve para indicar el panel administrativo qu el usuario mo pertenece al grupo de usuario que pueden acceder
    is_staff = models.BooleanField(default=False)


    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'correo'


    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

    objects = ManejoUsuario()

    class Meta:
        db_table = 'usuario'

class Mascota(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    sexo = models.TextField(choices=[('HEMBRA', 'hembra'),('MACHO', 'MACHO')])
    fechaNacimiento = models.DateField(db_column='fecha_nacimiento')
    alergias = models.TextField()
    alergias = models.TextField(null=False)