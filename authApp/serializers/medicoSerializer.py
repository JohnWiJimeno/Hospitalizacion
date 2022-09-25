from rest_framework import serializers
from authApp.models.medico import Medico


class MedicoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Medico
        fields = ['idmedico', 'nombre', 'apellido', 'telefono','correo', 'especialidad','genero','user']

