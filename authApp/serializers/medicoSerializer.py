from rest_framework import serializers
<<<<<<< HEAD
from authApp.models.medico import Medico


class medicoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Medico
        fields = ['idmedico', 'nombre', 'apellido', 'telefono','correo', 'especialidad','idusuario']
=======
from authApp.models.medico import medico


class medicoSerializer(serializers.ModelSerializer):

    class Meta:
        model: medico
        fields = ['idmedico', 'nombre', 'apellidos','telefono', 'email', 'especialidad', 'genero', 'user']
>>>>>>> 1c1cd8f73bb1a6ef8b6ec98743bacdee4c011e66
