from rest_framework import serializers
from authApp.models.familiar import Familiar


class familiarSerializer(serializers.ModelSerializer):

    class Meta:
        model: Familiar
        fields = ['idfamiliar', 'nombre', 'apellidos','parentesco', 'email','telefono']