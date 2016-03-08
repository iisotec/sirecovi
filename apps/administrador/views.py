from django.shortcuts import render_to_response, RequestContext
from .models import Visitante, Oficina
# Create your views here.
def Index_principal(request):
	return render_to_response('administrador/index.html', context=RequestContext(request))	

def Index_view(request):
	return render_to_response('administrador/control/index.html', context=RequestContext(request))	

def Visitante_views(request):
	datos = Visitante.objects.all()[:5]
	#return render_to_response('index.html',{'datos':visitantes})
	return render_to_response('administrador/control/visitante.html', {'v_visitantes':datos})	

def Oficina_views(request):
	return render_to_response('administrador/control/oficina.html', context=RequestContext(request))		