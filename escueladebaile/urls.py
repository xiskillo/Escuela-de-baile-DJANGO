"""escueladebaile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url
from noticias.urls import noticias_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nucleo.urls')),
    path('noticias/', include (noticias_patterns)),    
    path('accounts/', include ('django.contrib.auth.urls')),
    path('accounts/', include ('registration.urls')),
    path('contactar/', include ('contactar.urls')),
    path('clases/', include ('clases.urls')),
]


#PARA PERMITIR A DJANGO GESTIONAR LAS FOTOS EN MODO DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   import debug_toolbar
   urlpatterns=urlpatterns+ [url(r'^__debug__/', include(debug_toolbar.urls)),]


#urlpatterns=urlpatterns+ [url(r'^captcha/', include('captcha.urls')),]