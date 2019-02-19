from django.contrib import admin
from .models import Profesores, Aulas

# Register your models here.

class ProfesoresAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



class AulasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(Profesores, ProfesoresAdmin)
admin.site.register(Aulas, AulasAdmin)