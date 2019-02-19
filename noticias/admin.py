from django.contrib import admin
from .models import Noticia

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')



admin.site.register(Noticia, NoticiaAdmin)