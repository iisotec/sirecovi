from django.db import models

# Create your models here.
class Visitante(models.Model):
	"""docstring for visitante"""
	dni = models.CharField(max_length=8)
	nombres = models.CharField(max_length=80, help_text='Nombres')
	apellidos = models.CharField(max_length=120, help_text='Apellidos')
	fecha_visita = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.nombres

class Oficina(models.Model):
	"""docstring for visitante"""
	nombre = models.CharField(max_length=120, help_text='Nombre')
	estado = models.BooleanField(default=False)
	visit_oficina = models.ManyToManyField(Visitante)

	def __unicode__(self):
		return self.nombre

'''class visita_oficina(models.Model):
	"""docstring for visitante"""
	dni = models.IntegerField(max_length=8, label='Dni')
	nombre = models.TextField(max_length=120, label='Nombre')
	estado = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.nombre '''
