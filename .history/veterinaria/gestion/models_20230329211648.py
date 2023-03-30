from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)

    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False) 
    password = models.TextField(null=False) 
    # CharFiel
    tipoUsuario = models.CharField(max_length=100, choices=[('ADMIN','ADMIN'),('CLIENTE','CLIENTE')],
    db_column='tipo_usuario')

    is_staff = models.BooleanField(default=False)


    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'correo'


    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        db_table = 'usuario'