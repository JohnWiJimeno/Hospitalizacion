from rest_framework import serializers
from authApp.models.sugerencia import Sugerencia


class sugerenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model: Sugerencia
<<<<<<< HEAD
        fields = ['idsugerencia', 'entorno', 'fecha', 'sugerencia', 'descripcion']
=======
        fields = ['idsugerencia', 'entorno', 'fecha', 'sugerencia', 'descripcion']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
