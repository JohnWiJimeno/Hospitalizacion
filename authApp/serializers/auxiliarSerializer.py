from rest_framework import serializers
from authApp.models.auxiliar import Auxiliar


class auxiliarSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
   
    class Meta:
        model = Auxiliar
        fields = ['idauxiliar', 'nombre', 'apellido', 'correo', 'telefono','idusuario']
=======

    class Meta:
        model: Auxiliar
        fields = ['idauxiliar', 'nombre', 'apellidos', 'telefono', 'email', 'genero', 'user']
>>>>>>> 1c1cd8f73bb1a6ef8b6ec98743bacdee4c011e66
