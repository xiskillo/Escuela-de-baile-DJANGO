from django.urls import path
from . import views
from .views import NoticiaListView,NoticiaDetailView,NoticiaCreate,NoticiaUpdate,NoticiaDelete


"""
urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<int:noticia_id>/<slug:noticia_slug>/', views.noticia, name='noticia'),
]
"""

noticias_patterns = ([
    path('', NoticiaListView.as_view(), name='noticias'),
    path('<int:pk>/<slug:slug>/', NoticiaDetailView.as_view(), name='noticia'),
    path('create/', NoticiaCreate.as_view(), name='create'),
    path('update/<int:pk>/', NoticiaUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', NoticiaDelete.as_view(), name='delete'),
],'noticias')