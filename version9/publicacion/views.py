from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .models import publicacion, Comentario
from .forms import NoticiaForm
from django.views.generic.detail import DetailView

from publicacion import models


# Create your views here.
def saludo(request):
    return HttpResponse("bienbenido este es mi blog")

class Listar(ListView):
	
	model=publicacion
	template_name = "listado.html"
	context_object_name = "publicaciones"

class Detalle(DetailView):
	model=publicacion
	template_name="detalle.html"

class quees19(ListView):
	
	model=publicacion
	template_name = "paginaexplicacion.html"
	context_object_name = "publicaciones"
class Updatepublicacion(UpdateView):
	model = publicacion
	template_name = "publicacion/publicacion_form.html"
	success_url='http://127.0.0.1:8000/'
	fields=['autor', 'titulo', 'contenido', 'fecha_creacion']

class borrarpublicacion(DeleteView):
	model=publicacion
	success_url = 'http://127.0.0.1:8000/'



class Crearpublicacion(CreateView):
	model=publicacion
	template_name = "noticia_form.html"
	success_url="http://127.0.0.1:8000/"
	fields= ['autor', 'titulo','contenido', 'fecha_creacion']



