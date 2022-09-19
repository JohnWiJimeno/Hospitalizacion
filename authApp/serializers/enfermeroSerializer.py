from rest_framework import serializers
from authApp.models.enfermero import enfermero


class enfermeroSerializer(serializers.ModelSerializer):

    class Meta:
        model: enfermero
        fields = ['idenfermero', 'nombre', 'apellidos', 'telefono', 'email', 'genero', 'user']