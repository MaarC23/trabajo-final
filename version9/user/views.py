from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from .models import User
class Crearpublicacion(CreateView):
	model=User
	success_url="http://127.0.0.1:8000/"
	fields= ['first_name', 'last_name', 'email', 'password']
