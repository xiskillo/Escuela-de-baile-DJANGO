from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Noticia
from .forms import NoticiaForm
# Create your views here.


"""PARA COMPROBAR SI SE ESTA REGISTRADO O NO"""
class ComprobarRegistro(object):
    
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        
        return super(ComprobarRegistro, self).dispatch(request, *args, **kwargs)



"""
def noticias(request):
    noticias = get_list_or_404(Noticia)
    return render(request, 'noticias/noticias.html', {'noticias':noticias})
"""

class NoticiaListView(ListView):
    model=Noticia


"""
def noticia(request, noticia_id, noticia_slug):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticias/noticia.html', {'noticia':noticia})

"""


class NoticiaDetailView(DetailView):
    model=Noticia


@method_decorator(staff_member_required, name='dispatch')
class NoticiaCreate(CreateView):
    model = Noticia
    #importamos desde el formulario y podemos quitar los fields esta vez 
    form_class=NoticiaForm

    #fields = ['titulo','contenido','orden']
    success_url=reverse_lazy('noticias:noticias')
  

@method_decorator(staff_member_required, name='dispatch')
class NoticiaUpdate(UpdateView):
    model = Noticia
    fields = ['titulo','contenido','orden']
    template_name_suffix='_update_form'
    success_url=reverse_lazy('noticias:noticias')

    
@method_decorator(staff_member_required, name='dispatch')
class NoticiaDelete(DeleteView):
    model = Noticia
    success_url=reverse_lazy('noticias:noticias')
   
   

