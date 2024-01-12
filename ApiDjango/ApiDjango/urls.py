"""
URL configuration for ApiDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from api.views import Home 
from api.views import LoginE
from api.views import LoginC 
from api.views import Registro
from api.views import Problema 
from api.views import Registro_ClienteView  
from api.views import LoginView
from api.views import ProblemasClienteView
from api.views import AdminB
from api.views import RegistroEmpleados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('Login_Empleado',LoginE.as_view(),name='Login_Empleado'),
    path('Login_Cliente',LoginC.as_view(),name='Login_Cliente'),
    path('Registro',Registro.as_view(),name='Registro'),
    path('Problema',Problema.as_view(),name='Problema'),
    path('Registro_Cliente/',Registro_ClienteView.as_view(),name='Registro_Cliente'),
    path('Admin/',AdminB.as_view(),name='Admin'),
    path('RegistroEmpleados/',RegistroEmpleados.as_view(),name='RegistroEmpleados'),
    path('loginView/', LoginView.as_view(), name='loginview'),
    path('ProblemaView/', ProblemasClienteView.as_view(), name='Problemaview'),
] 
