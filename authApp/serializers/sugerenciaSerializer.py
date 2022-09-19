from rest_framework import serializers
from authApp.models.sugerencia import sugerencia


class sugerenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model: sugerencia
        fields = ['idsugerencia', 'entorno', 'fecha', 'sugerencia', 'descripcion']