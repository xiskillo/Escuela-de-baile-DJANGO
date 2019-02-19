from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationFormEmail


# Create your views here.
class RegistrarView(CreateView):
    
    form_class=UserCreationFormEmail
    success_url=reverse_lazy('login')
    template_name='registration/registrar.html'