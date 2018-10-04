from django.core.management.base import BaseCommand

from users.models import Usuario


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("*-------------- Bienvenido a nuestra red social ------------")
        print("1. crear usuario \n2. Listar usuarios \n3. Acceder \n4.Salir")
        decition = input("Ingrese el numero de la accion que desea realizar: ")
        if(int(decition) == 1):
        	name = input("ingrese su primer nombre: ")
        	apellido = input("ingrese su apellido: ")
        	email = input("ingrese su email: ")
        	username = input("ingrese su nombre de usuario: ")
        	new_user = Usuario(primer_nombre=name,apellido=apellido,email=email,username=username)
        	new_user.save()
        	print("*ahi vamos*")
        else:
        	print("ahhh y de ahi?")