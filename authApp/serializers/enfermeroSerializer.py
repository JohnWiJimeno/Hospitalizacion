from rest_framework import serializers
from authApp.models.enfermero import Enfermero


class EnfermeroSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Enfermero
        fields = ['idenfermero','nombre','apellidos','telefono','email','genero','user_id']

