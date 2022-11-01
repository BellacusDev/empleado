from django.contrib import admin
from django.urls import path
from . import views


app_name = 'persona_app'


urlpatterns = [
    #inicio
    path('',
         views.InicioView.as_view(),
         name='inicio'),

    path('admin/', admin.site.urls),
    path('listar-todo-empleados/',
         views.ListAllEmpleados.as_view(),
         name='empleados_all'),
    path(
        'list-by-area/<shorname>/',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'buscar-empleado/',
        views.ListEmpleadosByKword.as_view()
    ),
    path(
        'listar-habilidades-empleado/',
        views.ListHabilidadesEmpleado.as_view()
    ),
    path(
        'ver-empleado/<pk>',
         views.EmpleadoDetailview.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),

    path('success/',
         views.SuccessView.as_view(),
         name='correcto'
         ),
    path('editar-empleado/<pk>',
         views.EmpleadoUpdateView.as_view(),
         name='modificar_empleado'),
    path('eliminar-empleado/<pk>',
         views.EmpleadoDeleteView.as_view(),
         name='eliminar_empleado'),
    path('lista-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(),
         name='empleados_admin'),

]