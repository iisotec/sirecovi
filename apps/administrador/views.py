from django.shortcuts import render_to_response, RequestContext, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from apps.oficina.models import  Oficina
from apps.recepcion.models import  Visitante
from apps.users.models import User

from apps.users.models import User
from .forms import VisitanteForm, OficinaForm
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.
def Index_principal(request):
	return render_to_response('administrador/index.html', context=RequestContext(request))	

def Index_view(request):
	return render_to_response('administrador/control/index.html', context=RequestContext(request))	
# mostrando todas la visitantes
def Visitante_views(request):
	datos = Visitante.objects.order_by('-fecha_registro')[:15].all()
	return render_to_response('administrador/control/visitante.html', {'v_visitantes':datos})	

def OficinaA_views(request):
	datos = Oficina.objects.order_by('-nombre')[:15].all()
	return render_to_response('administrador/control/oficina.html', {'v_oficinas': datos})

#class OficinaA_views(TemplateView):

 #   template_name = 'administrador/control/oficina.html'

#    def get_context_data(self, **kwargs):
 #       context = super(OficinaA_views, self).get_context_data(**kwargs)
  #      context['v_oficinas'] = Oficina.objects.all()
        #context['cantidad'] = context['administrador'].count()
   #     return context


def UsuariosA_views(request):
    datos = User.objects.order_by('-last')[:15].all()
    return render_to_response('administrador/control/usuarios.html', {'v_usuarios':datos})

class CreateOficina(CreateView):
    form_class = OficinaForm
    template_name = 'administrador/control/crear_oficina.html'
    success_url = reverse_lazy('administrador_app:p_oficina')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CreateOficina, self).form_valid(form)

class OficinaEdit(UpdateView):
    template_name = 'administrador/control/editar_oficina.html'
    success_url = reverse_lazy('administrador_app:p_oficina')
    model = Oficina
    form_class = OficinaForm

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(OficinaEdit, self).form_valid(form)


#     return render(request, "events/panel/crear_evento.html", {"form": modelform})
class CreateVisitante(CreateView):

    form_class = VisitanteForm
    template_name = 'administrador/control/crear_visitante.html'
    success_url = reverse_lazy('administrador_app:p_visitante')

    def form_valid(self, form):
        #form.instance.organizer = self.request.user
        return super(CreateVisitante, self).form_valid(form)

class VisitanteEdit(UpdateView):

    template_name = 'administrador/control/editar_evento.html'
    success_url = reverse_lazy('events_app:panel')
    model = Visitante
    form_class = VisitanteForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)

#     return render(request, "events/panel/eliminar_evento.html", {'event': event})
class VisitanteDelete(DeleteView):
    template_name = 'events/panel/eliminar_evento.html'
    model = Visitante
    success_url = reverse_lazy('events_app:panel')
    context_object_name = 'event'

