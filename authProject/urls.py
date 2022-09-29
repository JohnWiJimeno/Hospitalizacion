"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
<<<<<<< HEAD

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
=======
#from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views



urlpatterns = [
    #path('admin/', admin.site.urls),
>>>>>>> 36d994949627123dfbbf025f32099bc54f8c969a
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
<<<<<<< HEAD
    path('enfermero/', views.enfermero_api_view),
    path('enfermero/<int:pk>',views.enfermero_detail_view),
    path('familiar/', views.familiar_api_view),
    path('familiar/<int:pk>',views.familiar_detail_view),
    path('auxiliar/', views.auxiliar_api_view),
    path('auxiliar/<int:pk>',views.auxiliar_detail_view),
    path('medico/', views.medico_api_view),
    path('medico/<int:pk>',views.medico_detail_view),
    path('paciente/', views.paciente_api_view),
    path('paciente/<int:pk>',views.paciente_detail_view),
    path('historia/', views.historia_api_view),
    path('historia/<int:pk>',views.historia_detail_view),
    path('signosvitales/', views.signosvitales_api_view),
    path('signosvitales/<int:pk>',views.signosvitales_detail_view),
    path('detallesignos/', views.detallesignos_api_view),
    path('detallesignos/<int:pk>',views.detallesignos_detail_view),
    path('sugerencia/', views.sugerencia_api_view),
    path('sugerencia/<int:pk>',views.sugerencia_detail_view)
]
=======
    path('auth/',include('authApp.urls'))
    #path('enfermero/', views.enfermero_api_view),
    #path('enfemero/<int:pk>',views.enfermero_detail_view)

]
>>>>>>> 36d994949627123dfbbf025f32099bc54f8c969a
