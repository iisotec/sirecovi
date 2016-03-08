from django.shortcuts import render_to_response, RequestContext

# Create your views here.
def Index_principal(request):
	return render_to_response('administrador/index.html', context=RequestContext(request))	

def Index_view(request):
	return render_to_response('administrador/control/index.html', context=RequestContext(request))	

def Visitante(request):
	return render_to_response('administrador/control/visitante.html', context=RequestContext(request))	

def Oficina(request):
	return render_to_response('administrador/control/oficina.html', context=RequestContext(request))		