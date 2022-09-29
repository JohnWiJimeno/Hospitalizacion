from rest_framework import serializers
from authApp.models.sugerencia import Sugerencia


class SugerenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sugerencia
        fields = ['idsugerencia', 'entorno', 'fecha', 'sugerencia', 'descripcion']
