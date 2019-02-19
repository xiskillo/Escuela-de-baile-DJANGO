from django.urls import path
from . import views


urlpatterns=[
    path('', views.clases, name="clases"),
    path('profesores/<int:profesores_id>/', views.profesores, name="profesores") 
]