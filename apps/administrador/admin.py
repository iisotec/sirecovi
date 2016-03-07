from django.contrib import admin
from .models import Visitante, Oficina
from .actions import export_as_excel

# Register your models here.
@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
	list_display = ('dni','nombres','apellidos','fecha_visita')
	search_fields = ('dni', 'nombres','apellidos',)
	list_filter = ('fecha_visita',)
	actions = [export_as_excel,]

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	list_display = ('nombre','estado')
