from django.db import models
from django.conf import settings

# Create your models here.
class Oficina(models.Model):
	"""docstring for visitante"""
	nombre = models.CharField(max_length=120, unique=True, help_text='Nombre')
	estado_oficina = models.BooleanField(default=False)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

	def __unicode__(self):
		return self.nombre
