# Register your models here.
from django.contrib import admin
from .models import  Oficina
from .actions import export_as_excel

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	list_display = ('nombre','estado')
