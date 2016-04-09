from django.db import models
from apps.oficina.models import Oficina
# Create your models here.

class Visitante(models.Model):
	"""docstring for visitante"""
	dni = models.CharField(max_length=8, unique=True, db_index=True)
	nombres = models.CharField(max_length=80, help_text='Nombres')
	apellidos = models.CharField(max_length=120, help_text='Apellidos')
	fecha_registro = models.DateTimeField(auto_now_add=True)
	oficinas = models.ManyToManyField(Oficina, through='VisitanteOficina', blank=True)

	
	def __unicode__(self):
		return self.nombres

class VisitanteOficina(models.Model):
	#oficina = models.ForeignKey(Oficina,on_delete=models.CASCADE)
	oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
	visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
	fecha_visita = models.DateTimeField(auto_now_add=True)
	estado_atencion = models.BooleanField(default=False)
	sesion = models.BooleanField()

	def __unicode__(self):
		return self.oficina.nombre
