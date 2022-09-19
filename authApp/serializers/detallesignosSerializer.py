from rest_framework import serializers
from authApp.models.detallesignos import detallesignos


class detallesignosSerializer(serializers.ModelSerializer):

    class Meta:
        model: detallesignos
        fields = ['iddetalle', 'idsignosvitales', 'idpaciente', 'detalle']