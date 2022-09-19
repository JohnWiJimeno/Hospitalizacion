from rest_framework import serializers
from authApp.models.historia import historia


class historiaSerializer(serializers.ModelSerializer):

    class Meta:
        model: historia
        fields = ['idhistoria', 'idpaciente', 'idsugerencia','encasa']