from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Usuario

class SoloClientes(BasePermission):
    message = 'Solo los clientes pueden  realizar esta peticion'

    def has_permission(self, request: Request, view):
        # request.user > toda la informacion del usuario autenticado

        usuario : Usuario = request.user

        # utilizando un operador ternario
         #return True if usuario.tipoUsuario == 'CLIENTE' else False

        if usuario.tipoUsuario == 'CLIENTE':
            # si retornamos True indicaque el usuario tiene los permisos correspodientes           
            return True
        else:
            return False
        