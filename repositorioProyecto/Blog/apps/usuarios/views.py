from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm

class Registro(CreateView):
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'

def Usuario(request):
    return render(request,'usuarios/login.html')
# Create your views here.

