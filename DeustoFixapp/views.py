from django.shortcuts import render
from django.views.generic import View, ListView
from django.urls import reverse
from django.views.generic import TemplateView

from DeustoFixapp.forms import IncidenciaForm
from DeustoFixapp.models import Incidencia


# Create your views here.

class MenuPrincipalView(View):
    def get(self, request):
        return render(request, "inicio.html")

#Incidencia

class IncidenciaListViews(ListView):
    model = Incidencia
    template_name = 'DeustoFixapptemp/incidencia_list.html'


class IncidenciaCreateView(View):
    def get(self, request):
        formulario = IncidenciaForm()
        context = {'formulario': formulario}
        return render(request, 'DeustoFixapptemp/create_incidencia.html')
