from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Usuario

class SoloClientes(BasePermission):
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
        