from django.shortcuts import render, get_object_or_404
from .models import Aulas, Profesores

# Create your views here.



def clases(request):  
       
    aulas=Aulas.objects.all()
    return render(request, "clases/clases.html", {'aulas':aulas})


def profesores(request, profesores_id):
    profesores=Profesores.objects.get(id=profesores_id) 
    aulas=Aulas.objects.filter(profesores=profesores)   
    
    return render (request, "clases/clases_profesores.html", {'profesores':profesores})

    