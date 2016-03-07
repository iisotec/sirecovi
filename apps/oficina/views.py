from django.shortcuts import render

# Create your views here.
def Index_view(request):
	return render_to_response('oficina/index.html', context=RequestContext(request))	