from rest_framework import serializers
<<<<<<< HEAD

=======
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
from authApp.models.medico import Medico


class medicoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Medico
<<<<<<< HEAD
        fields = ['idmedico', 'nombre', 'apellido', 'telefono','correo', 'especialidad','genero','user']

=======
        fields = ['idmedico', 'nombre', 'apellidos', 'telefono','correo', 'especialidad','user']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
