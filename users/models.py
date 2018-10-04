from django.db import models

# Create your models here.
class Usuario(models.Model):
	primer_nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	username = models.CharField(max_length=20)
	#posts foreign key 
