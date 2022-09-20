from rest_framework import serializers
from authApp.models.enfermero import enfermero


class enfermeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enfermero
        fields = ['idenfermero', 'nombre', 'apellido', 'correo', 'telefono','idusuario']
