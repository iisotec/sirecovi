from django.contrib import admin
from .models import Visitante
from .actions import export_as_excel

# Register your models here.
@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
	list_display = ('dni','nombres','apellidos','fecha_registro')
	search_fields = ('dni', 'nombres','apellidos',)
	list_filter = ('fecha_registro',)
	actions = [export_as_excel,]