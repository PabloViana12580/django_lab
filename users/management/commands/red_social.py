from django.core.management.base import BaseCommand

from users.models import Usuario
from users.models import Post


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        whileThis = True
        menuUser = False
        post = False
        #usuarios = Usuario.objects.all()
        while(whileThis):
	        print("\n*-------------- Menu principal ------------")
	        print("1. crear usuario \n2. Listar usuarios \n3. Acceder \n4. Salir")
        	decition = input("Ingrese el numero de la accion que desea realizar: \n")
        	
	        if(int(decition) == 1):
	        	name = input("ingrese su primer nombre: ")
	        	apellido = input("ingrese su apellido: ")
	        	email = input("ingrese su email: ")
	        	username = input("ingrese su nombre de usuario: ")
	        	new_user = Usuario(primer_nombre=name,apellido=apellido,email=email,username=username)
	        	new_user.save()
	        elif int(decition) == 2:
	        	print("\n*-------------- Listado de nuestros usuarios ------------")
	        	usuarios = Usuario.objects.all()
	        	for userIt in usuarios:
	        		print("pk="+str(userIt.id)+":  "+userIt.primer_nombre+" "+userIt.apellido+" - "+userIt.email+ " - username: "+userIt.username)
	        elif int(decition) == 3:
	        	email = input("ingrese su email: ")
	        	username = input("ingrese su nombre de usuario: ")
	        	user_list = Usuario.objects.all()
	        	for userIt in user_list:
	        		if(userIt.username==username and userIt.email==email):
	        			post = True
	        			id_user = userIt.id
	        			print("Bienvenido "+ userIt.primer_nombre)
	        	while(post):
	        		print("\n*-------------- Menu de "+ username +" ------------")
	        		print("1. crear post \n2. Like post \n3. Borrar post \n4. Menu principal")
	        		decitionUser = input("Ingrese el numero de la accion que desea realizar: \n")
	        		if int(decitionUser) == 1:
	        			titulo = input("Ingrese el titulo: ")
	        			contenido = input("Escribe que quieres comunicar: ")
	        			new_post = Post(titulo=titulo,contenido=contenido,likes=0,author=Usuario.objects.get(username=username))
	        			new_post.save()
	        		elif int(decitionUser) == 2:
	        			user_post = Post.objects.all()
	        			for post in user_post:
	        				print("\n*-------------- post ------------*")
	        				print("titulo: " + post.titulo + "- contenido: " + post.contenido + "- id: "+ str(post.id) + "- likes: " + str(post.likes))
	        			id_post = input("\nElige el id del post al que quieras darle like: ")
	        			try:
	        				post_liked = Post.objects.get(id=id_post)
	        				post_liked.likes = post_liked.likes + 1
	        				post_liked.save()
	        				print("Le has dado like al post "+str(id_post)+"!")
	        			except Exception as e:
	        				print("No es un id valido, intente de nuevo")
	        		elif int(decitionUser) == 3:
	        			print("\n*-------------- post de " + username +" ------------")
	        			post_usuario_especifico = Post.objects.filter(author=id_user)
	        			for p_esp in post_usuario_especifico:
	        				print("id: " + str(p_esp.id) + " titulo: " + p_esp.titulo)
	        			delid_post = input("Escriba el id del post que desea borrar: ")
	        			try:
	        				post_del = Post.objects.get(id=delid_post)
	        				post_del.delete()
	        			except Exception as e:
	        				print("No es un id valido, pruebe nuevamente")
	        		elif int(decitionUser) == 4:
	        			post = False
	        	if(post==False):
	        		print("No se reconoce este usuario, pruebe nuevamente") 

	        elif int(decition) == 4:
	        	whileThis=False
	        	print("Gracias por usar el programa")
	        else:
	        	print("Fatal error")