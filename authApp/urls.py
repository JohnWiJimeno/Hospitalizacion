from django.urls import path
from .views import EnferView

urlpatterns = [
    path('enfermero/',EnferView.as_view(),name='EnfermeroView'),
    path('enfermero/<int:pk>',EnferView.as_view(),name='Enfermero_process'),
]
