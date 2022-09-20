from rest_framework import serializers
from authApp.models.auxiliar import Auxiliar


class auxiliarSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = Auxiliar
        fields = ['idauxiliar', 'nombre', 'apellido', 'correo', 'telefono','user']
<<<<<<< HEAD



=======
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
