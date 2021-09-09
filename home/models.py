from django.db import models
from login import models as login_models

# Create your models here.
class Estado(models.Model):
	estado = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Cita(models.Model):
	tarea = models.CharField(max_length=40)
	fecha = models.DateField()
	estado=models.ForeignKey(Estado, related_name="estados", on_delete=models.CASCADE)
	usuario=models.ForeignKey(login_models.User, related_name="usuario", on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)