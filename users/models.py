from django.db import models

# Create your models here.
class Usuario(models.Model):
	primer_nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	username = models.CharField(max_length=20)

class Post(models.Model):
	titulo = models.CharField(max_length=40)
	contenido = models.CharField(max_length=200)
	likes = models.IntegerField()
	author = models.ForeignKey(Usuario, on_delete=models.CASCADE)