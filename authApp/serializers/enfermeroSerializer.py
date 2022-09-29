from rest_framework import serializers
from authApp.models.enfermero import Enfermero


class EnfermeroSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Enfermero
<<<<<<< HEAD
        fields = ['idenfermero', 'nombre', 'apellidos', 'telefono', 'email', 'genero','user']
=======
        fields = ['idenfermero','nombre','apellidos','telefono','email','genero','user_id']
>>>>>>> 36d994949627123dfbbf025f32099bc54f8c969a

