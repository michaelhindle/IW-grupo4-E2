from django.urls import path
from . import views
from .views import (MenuPrincipalView, IncidenciaMenuView, IncidenciaListView, IncidenciaCreateView,
                    IncidenciaUpdateView, IncidenciaDeleteView)

urlpatterns = [
    # menu principal.

    path('', MenuPrincipalView.as_view, name='menu_principal'),

    # urls de incidencia.

    path('menu_incidencia', IncidenciaMenuView, name='incidencia'),
    path('menu_incidencia', IncidenciaMenuView.as_view(), name='incidencia_menu'),
    path('menu_incidencia', IncidenciaListView.as_view(), name='incidencia_menu'),
    path('create_incidencia', IncidenciaCreateView.as_view(), name='incidencia_create'),
    path('update_incidencia/<int:pk>', IncidenciaUpdateView.as_view(), name='update_incidencia'),
    path('delete_incidencia/<int:pk>', IncidenciaDeleteView.as_view(), name='delete_incidencia'),

    # urls de Instalacion

    # urls de Empleados
]
