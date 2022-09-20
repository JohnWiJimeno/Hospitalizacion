from rest_framework import serializers
from authApp.models.enfermero import Enfermero


class enfermeroSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Enfermero
        fields = ['idenfermero', 'nombre', 'apellido', 'correo', 'telefono','user']

