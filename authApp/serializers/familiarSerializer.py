from rest_framework import serializers
from authApp.models.familiar import familiar


class familiarSerializer(serializers.ModelSerializer):

    class Meta:
        model: familiar
        fields = ['idfamiliar', 'nombre', 'apellidos','parentesco', 'email','telefono']