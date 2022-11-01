from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )
from .models import Empleado
from django.urls import reverse_lazy
from .forms import EmpleadoForm

# Create your views here.


class InicioView(TemplateView):
    """ vista que carga la pagina de inicio"""
    template_name = 'inicio.html'




class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 2
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        print(Empleado.objects)
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list-by-area.html'
    context_object_name = 'empleados'


    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    model = Empleado
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'



class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/listar-habilidades-empleado.html/'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()


class EmpleadoDetailview(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailview, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def Form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoDetailview, self.form_valid(form))



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/update.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)




class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')


