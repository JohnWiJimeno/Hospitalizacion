from rest_framework import serializers
from authApp.models.medico import medico


class medicoSerializer(serializers.ModelSerializer):

    class Meta:
        model: medico
        fields = ['idmedico', 'nombre', 'apellidos','telefono', 'email', 'especialidad', 'genero', 'user']