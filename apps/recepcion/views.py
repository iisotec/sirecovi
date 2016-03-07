from django.shortcuts import render_to_response, RequestContext

# Create your views here.
def Index_view(request):
	return render_to_response('recepcion/index.html', context=RequestContext(request))	