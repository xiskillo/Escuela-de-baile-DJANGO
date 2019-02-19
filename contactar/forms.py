from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from ckeditor.fields import RichTextField


class ContactarForm(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="EMAIL", required=True)
    mensaje=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje'}))
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    

