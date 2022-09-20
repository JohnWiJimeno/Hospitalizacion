from rest_framework import serializers
from authApp.models.signosvitales import Signosvitales


class signosvitalesSerializer(serializers.ModelSerializer):

    class Meta:
        model: Signosvitales
        fields = ['idsignosvitales', 'nombre']
