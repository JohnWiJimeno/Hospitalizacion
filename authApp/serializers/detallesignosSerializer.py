from rest_framework import serializers
from authApp.models.detallesignos import Detallesignos


class detallesignosSerializer(serializers.ModelSerializer):

    class Meta:
        model: Detallesignos
<<<<<<< HEAD
        fields = ['iddetalle', 'idsignosvitales', 'idpaciente', 'detalle']
=======
        fields = ['iddetalle', 'idsignosvitales', 'idpaciente', 'detalle']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
