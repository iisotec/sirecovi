from django.shortcuts import render_to_response, RequestContext, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Visitante
from apps.users.models import User
from .forms import VisitanteForm
#import json
from .htmltopdf import render_to_pdf

from django.core.urlresolvers import reverse, reverse_lazy
# Create your views here.
def Index_view(request):
	return render_to_response('recepcion/index.html', context=RequestContext(request))	
# mostrando todas la visitantes
def Visitante_views(request):
	datos = Visitante.objects.order_by('-fecha_registro')[:15].all()
	return render_to_response('recepcion/control/visitante.html', {'vo_visitantes':datos})	

class CreateVisitante(CreateView):

    form_class = VisitanteForm
    template_name = 'recepcion/control/crear_visitante.html'
    success_url = reverse_lazy('recepcion_app:p_visitante')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateVisitante, self).form_valid(form)

class VisitanteEdit(UpdateView):
    template_name = 'recepcion/editar_evento.html'
    success_url = reverse_lazy('recepcion_app:p_visitante')
    model = Visitante
    form_class = VisitanteForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)

class VisitanteEdit(UpdateView):

    template_name = 'recepcion/editar_visitante.html'
    success_url = reverse_lazy('recepcion_app:p_visitante')
    model = Visitante
    form_class = VisitanteForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)

#     return render(request, "events/panel/eliminar_evento.html", {'event': event})
class VisitanteDelete(DeleteView):
    template_name = 'recepcion/eliminar_visitante.html'
    model = Visitante
    success_url = reverse_lazy('recepcion_app:p_visitante')
    context_object_name = 'event'

def pdf(request):
    return render_to_pdf('recepcion/control/reportes.html',{'title':'Reportes con PDF'})

# def lista_visitantes(request):
#     if request.is_ajax:
#         search=request.POST.get('start','')

#         visitantes = Visitante.objects.filter(dni__icontains=search)
        
#         results=[]
#         for visita in visitantes:
#             visita_json={}
#             visita_json['label']=visita.nombres
#             visita_json['value']=visita.dni
#             results.append(visita_json)
 
#         data_json=json.dumps(results)

#     else:
#         data_json='fail'
#     mimetype="application/json"
#     return Http