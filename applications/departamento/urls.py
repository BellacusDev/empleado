from django.contrib import admin
from django.urls import path
from . import views
app_name = 'departamento_app'
urlpatterns = [
    path(
        'departamento-lista/',
        views.DepartamentoListView.as_view(),
        name='departamento_list'),
    path(
        'nuevo-departamento/',
        views.NewDepartamantView.as_view(),
        name='nuevo_departamento'),

]