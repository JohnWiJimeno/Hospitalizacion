from rest_framework import serializers
from authApp.models.historia import Historiaclinica


class HistoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Historiaclinica
        fields = ['idhistoria', 'idpaciente', 'idsugerencia','encasa']
