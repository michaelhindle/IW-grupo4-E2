from django.urls import path
from .views import (MenuPrincipalView, IncidenciaMenuView, IncidenciaListView, IncidenciaCreateView,
                    IncidenciaUpdateView, IncidenciaDeleteView, IncidenciaDetailView, EmpleadoMenuView,
                    EmpleadoListView, EmpleadoCreateView,
                    EmpleadoUpdateView, EmpleadoDeleteView, InstalacionMenuView, InstalacionCreateView,
                    InstalacionListView, InstalacionUpdateView, InstalacionDeleteView)

urlpatterns = [
    # menu principal.

    path('menu/', MenuPrincipalView.as_view(), name='menu_principal'),

    # urls de incidencia.

    path('menu_incidencia/', IncidenciaMenuView.as_view(), name='menu_incidencia'),
    path('list_incidencia/', IncidenciaListView.as_view(), name='list_incidencia'),
    path('create_incidencia/', IncidenciaCreateView.as_view(), name='create_incidencia'),
    path('update_incidencia/<int:pk>', IncidenciaUpdateView.as_view(), name='update_incidencia'),
    path('delete_incidencia/<int:pk>', IncidenciaDeleteView.as_view(), name='delete_incidencia'),
    path('incidencia_detail/<int:pk>', IncidenciaDetailView.as_view(), name='incidencia_detail'),

    # urls de Instalacion
    path('menu_instalacion/', InstalacionMenuView.as_view(), name='menu_instalacion'),
    path('list_instalacion/', InstalacionListView.as_view(), name='list_instalacion'),
    path('create_instalacion/', InstalacionCreateView.as_view(), name='create_instalacion'),
    path('update_instalacion/<int:pk>', InstalacionUpdateView.as_view(), name='update_instalacion'),
    path('delete_instalacion/<int:pk>', InstalacionDeleteView.as_view(), name='delete_instalacion'),

    # urls de Empleados

    path('menu_emplado/', EmpleadoMenuView.as_view(), name='menu_empleado'),
    path('list_empleado/', EmpleadoListView.as_view(), name='list_empleado'),
    path('create_empleado/', EmpleadoCreateView.as_view(), name='create_empleado'),
    path('update_empleado/<int:pk>', EmpleadoUpdateView.as_view(), name='update_empleado'),
    path('delete_empleado/<int:pk>', EmpleadoDeleteView.as_view(), name='delete_empleado')
]
