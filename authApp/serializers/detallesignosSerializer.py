from rest_framework import serializers
from authApp.models.detallesignos import Detallesignos


class DetallesignosSerializer(serializers.ModelSerializer):

    class Meta:
        model: Detallesignos
        fields = ['iddetalle', 'idsignosvitales', 'idpaciente', 'detalle']
