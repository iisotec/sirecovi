from django.shortcuts import render_to_response, RequestContext, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Oficina
from apps.users.models import User
from .forms import OficinaForm
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.
#def Index_view(request):
#	return render_to_response('oficina/index.html', context=RequestContext(request))	

def Oficina_views(request):
	datos = Oficina.objects.order_by('-nombre')[:15].all()
	return render_to_response('oficina/control/oficina.html', {'v_oficinas':datos})
    
class CreateOficina(CreateView):
    form_class = OficinaForm
    template_name = 'oficina/control/crear_oficina.html'
    success_url = reverse_lazy('oficina_app:apo_nuevo')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CreateOficina, self).form_valid(form)

class OficinaEdit(UpdateView):

    template_name = 'oficina/control/editar_oficina.html'
    success_url = reverse_lazy('oficina_app:panel')
    model = Oficina
    form_class = OficinaForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(OficinaEdit, self).form_valid(form)

class OficinaDelete(DeleteView):
    template_name = 'oficina/control/eliminar_visitante.html'
    model = Oficina
    success_url = reverse_lazy('oficina_app:panel')
    context_object_name = 'event'
