from rest_framework import serializers
from authApp.models.historia import Historia


class historiaSerializer(serializers.ModelSerializer):

    class Meta:
        model: Historia
        fields = ['idhistoria', 'idpaciente', 'idsugerencia','encasa']
