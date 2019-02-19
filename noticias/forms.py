from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model=Noticia
       
        fields=['titulo','contenido','orden']
        widgets={'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduce el Título'}),
                'contenido':forms.Textarea(attrs={'class':'form-control',}),
                'orden':forms.NumberInput(attrs={'class':'form-control',})
                }

        labels={'titulo':'Titula la noticia','orden':'Prioridad'}



