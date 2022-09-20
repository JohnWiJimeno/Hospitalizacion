from rest_framework import serializers
from authApp.models.medico import Medico


class medicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ['idmedico', 'nombre', 'apellidos', 'telefono','correo', 'especialidad','user']
