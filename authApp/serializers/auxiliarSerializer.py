from rest_framework import serializers
from authApp.models.auxiliar import Auxiliar


class AuxiliarSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = Auxiliar
        fields = ['idauxiliar', 'nombre', 'apellido', 'correo', 'telefono','user']
