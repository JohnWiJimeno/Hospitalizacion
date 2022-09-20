from rest_framework import serializers
from authApp.models.signosvitales import Signosvitales


class signosvitalesSerializer(serializers.ModelSerializer):

    class Meta:
        model: Signosvitales
<<<<<<< HEAD
        fields = ['idsignosvitales', 'nombre']
=======
        fields = ['idsignosvitales', 'nombre']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
