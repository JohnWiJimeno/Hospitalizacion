from rest_framework import serializers
<<<<<<< HEAD

=======
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
from authApp.models.enfermero import Enfermero


class enfermeroSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Enfermero
<<<<<<< HEAD
        fields = ['idenfermero', 'nombre', 'apellido', 'correo', 'telefono','user']

=======
        fields = ['idenfermero', 'nombre', 'apellidos', 'correo', 'telefono','user']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
