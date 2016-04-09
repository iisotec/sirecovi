from django.shortcuts import render_to_response, RequestContext, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Visitante, VisitanteOficina
from apps.users.models import User
from .forms import VisitanteForm, VisitanteOficinaForm
#import json
from .htmltopdf import render_to_pdf
from django.db.models import Q

from django.core.urlresolvers import reverse, reverse_lazy
# Create your views here.
def Index_view(request):
	return render_to_response('recepcion/index.html', context=RequestContext(request))	
# mostrando todas la visitantes a cada oficina
class Visitante_views(TemplateView):

    template_name = 'recepcion/control/visitante.html'

    def get_context_data(self, **kwargs):
        context = super(Visitante_views, self).get_context_data(**kwargs)
        context['vo_visitantes'] = VisitanteOficina.objects.order_by('-fecha_visita')[:15].all()
        context['cantidad'] = context['vo_visitantes'].count()
        return context

# def Visitante_views(request):
# 	datos = VisitanteOficina.objects.order_by('-fecha_visita')[:15].all()
# 	return render_to_response('recepcion/control/visitante.html', {'vo_visitantes':datos})	

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

class VisitanteRegister(CreateView):

    form_class = VisitanteOficinaForm
    template_name = 'recepcion/control/registrar_visitante.html'
    success_url = reverse_lazy('recepcion_app:p_visitante')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VisitanteRegister, self).form_valid(form)

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
#Buscador por DNI, Nombre y Apellidos
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(dni__icontains=query) |
            Q(nombres__icontains=query) |
            Q(apellidos__icontains=query)
        )
#        results = Visitante.objects.get(qset).distinct()
        results = Visitante.objects.filter(qset)
    else:
        results = []
    return render_to_response("recepcion/control/busqueda.html", {
        "resultados": results,
        "query": query
    })