from rest_framework import serializers
from authApp.models.signosvitales import signosvitales


class signosvitalesSerializer(serializers.ModelSerializer):

    class Meta:
        model: signosvitales
        fields = ['idsignosvitales', 'nombre']