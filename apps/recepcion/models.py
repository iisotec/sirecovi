from django.db import models
from apps.oficina.models import Oficina
# Create your models here.

class Visitante(models.Model):
	"""docstring for visitante"""
	dni = models.CharField(max_length=8, unique=True)
	nombres = models.CharField(max_length=80, help_text='Nombres')
	apellidos = models.CharField(max_length=120, help_text='Apellidos')
	fecha_registro = models.DateTimeField(auto_now_add=True)
	oficina = models.ManyToManyField(Oficina)

	def __unicode__(self):
		return self.nombres
