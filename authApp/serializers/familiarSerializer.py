from rest_framework import serializers
from authApp.models.familiar import Familiar


class familiarSerializer(serializers.ModelSerializer):

    class Meta:
        model: Familiar
<<<<<<< HEAD
        fields = ['idfamiliar', 'nombre', 'apellidos','parentesco', 'email','telefono']
=======
        fields = ['idfamiliar', 'nombre', 'apellidos','parentesco', 'email','telefono']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
