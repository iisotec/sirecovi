from django.shortcuts import render_to_response, RequestContext

# Create your views here.
def index_view(request):
	return render_to_response('visitantes/index.html', context=RequestContext(request))