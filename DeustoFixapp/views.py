from django.db.models import Q
from django.http import request, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView

from DeustoFixapp.forms import IncidenciaForm, EmpleadoForm
from DeustoFixapp.models import Incidencia, Empleado


# Create your views here.

# La view del menu principal

class MenuPrincipalView(View):
    def get(self, request):
        return render(request, "base.html")


# Las views de Incidencia
class IncidenciaMenuView(View):
    def get(self, request):
        return render(request, "DeustoFixappIncidencia/menu_incidencia.html")

    def list_incidencias(self):
        buscar = request.GET.get('buscar')
        incidencias = Incidencia.objects.all()
        if buscar:
            incidencias = incidencias.filter(
                Q(titulo__icontains=buscar) |
                Q(tipo__icontains=buscar)).distinct()
        return render(request, 'DeustoFixappIncidencia/list_incidencia.html', {'incidencias': incidencias})


# LISTA de incidencia
class IncidenciaListView(ListView):
    model = Incidencia
    template_name = 'DeustoFixappIncidencia/list_incidencia.html'
    context_object_name = "incidencias"
    


# CREAR de incidencia
class IncidenciaCreateView(View):
    def get(self, request):
        formulario = IncidenciaForm()
        return render(request, 'DeustoFixappIncidencia/create_incidencia.html', {'form': formulario})

    def post(self, request):
        formulario = IncidenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('menu_incidencia')
        return render(request, 'DeustoFixappIncidencia/create_incidencia.html', {'form': formulario})


# DETALLE de incidencia
class IncidenciaDetailView(View):
    def get(self, request, pk):
        incidencia = get_object_or_404(Incidencia, pk=pk)
        data = {
            'titulo': incidencia.titulo,
            'descripcion': incidencia.descripcion,
            'TIPO': incidencia.tipo,
            'URGENCIA': incidencia.nivel_urgencia,
            'estado': incidencia.estado
        }
        return render(request, 'DeustoFixappIncidencia/incidencia_detail.html', {'incidencia' : incidencia})


# ACTUALIZAR de incidencia
class IncidenciaUpdateView(View):
    def get(self, request, pk):
        incidencia = Incidencia.objects.get(pk=pk)
        formulario = IncidenciaForm(instance=incidencia)

        form = {'formulario': formulario,
                'titulo': incidencia
                }
        return render(request, 'DeustoFixappIncidencia/update_incidencia.html', form)

    def post(self, request, pk):
        incidencia = Incidencia.objects.get(pk=pk)
        formulario = IncidenciaForm(request.POST, instance=incidencia)
        form = {'formulario': formulario, 'titulo': incidencia}
        if formulario.is_valid():
            formulario.save()
            return redirect('menu_incidencia')
        return render(request, 'DeustoFixappIncidencia/update_incidencia.html', form)


# ELIMINAR de incidencia
class IncidenciaDeleteView(View):
    def get(self, request):
        incidencia_id = request.POST('incidencia_id')
        incidencia = get_object_or_404(Incidencia, pk=incidencia_id)
        return render(request, 'DeustoFixappIncidencia/menu_incidencia.html', {'incidencia': incidencia})

    def post(self, request, pk):
        incidencia = get_object_or_404(Incidencia, pk=pk)
        incidencia.delete()
        return redirect('menu_incidencias')

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


# Las views de Empleados
# MENU de empleados
class EmpleadoMenuView(View):
    def get(self, request):
        return render(request, 'DeustoFixappEmpleado/menu_empleado.html')

    def listar_empleados(request):
        buscar = request.POST.get("buscar")
        empleados = Empleado.objects.all()
        if buscar:
            empleados = empleados.objects.filter(
                Q(dni__icontains=buscar) |
                Q(nombre__icontains=buscar)
            ).distinct()

        return render(request, 'DeustoFixappEmpleado/menu_empleado.html', {"empleados": empleados})


# LISTA de empleado
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'DeustoFixappEmpleado/list_empleado.html'
    context_object_name = 'empleados'


# CREAR de emplado
class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        return render(request, 'DeustoFixappEmpleado/create_empleado.html', {"form": formulario})

    def post(self, request):
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('menu_empleado')
        return render(request, 'DeustoFixappEmpleado/create_empleado.html', {"form": formulario})


# DETALLE de empleado
class EmpleadoDetailView(View):
    def get(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        data = {
            'nombre': empleado.nombre,
            'apellido': empleado.apellidos,
            'email': empleado.email,
            'telefono': empleado.telefono
        }
        return JsonResponse(data)

#ACTUALIZAR de empleado
class EmpleadoUpdateView(View):
    def get(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        formulario = EmpleadoForm(instance=empleado)

        form = {'formulario': formulario,
                'nombre': empleado
                }
        return render(request, 'DeustoFixappEmpleado/update_empleado.html', form)

#ELIMINAR de empleado
class EmpleadoDeleteView(View):
    def get(self, request):
        empleado_id = request.POST.get('empleado_id')
        empleado = get_object_or_404(Empleado, pk= empleado_id)
        return render(request, 'DeustoFixappEmpleado/menu_empleado.html', {"empleado": empleado})

    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.delete()
        return redirect('menu_empleado')

