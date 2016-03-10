from django.shortcuts import render_to_response, RequestContext, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Visitante
from apps.users.models import User
from .forms import VisitanteForm
from django.core.urlresolvers import reverse, reverse_lazy
# Create your views here.
def Index_view(request):
	return render_to_response('recepcion/index.html', context=RequestContext(request))	
# mostrando todas la visitantes
def Visitante_views(request):
	datos = Visitante.objects.order_by('-fecha_visita')[:15].all()
	return render_to_response('recepcion/visitante.html', {'v_visitantes':datos})	

class CreateVisitante(CreateView):

    form_class = VisitanteForm
    template_name = 'events/panel/crear_evento.html'
    success_url = reverse_lazy('events_app:panel')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(CreateEvent, self).form_valid(form)

class VisitanteEdit(UpdateView):
    template_name = 'administrador/control/editar_evento.html'
    success_url = reverse_lazy('events_app:panel')
    model = Visitante
    form_class = VisitanteForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)

class VisitanteEdit(UpdateView):

    template_name = 'recepcion/editar_visitante.html'
    success_url = reverse_lazy('events_app:panel')
    model = Visitante
    form_class = VisitanteForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)

#     return render(request, "events/panel/eliminar_evento.html", {'event': event})
class VisitanteDelete(DeleteView):
    template_name = 'recepcion/eliminar_visitante.html'
    model = Visitante
    success_url = reverse_lazy('events_app:panel')
    context_object_name = 'event'
