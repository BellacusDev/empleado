from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import New_DepartamentForm
from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.

class DepartamentoListView(ListView):
    model= Departamento
    template_name = 'departamento/lista.html'
    context_object_name = 'departamentos'

class NewDepartamantView(FormView):
    template_name = 'departamento/nuevo-departamento.html'
    form_class = New_DepartamentForm
    success_url = '/'
    
    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname'],
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento = depa

        )
        return super(NewDepartamantView, self).form_valid(form)
