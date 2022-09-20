from rest_framework import serializers
from authApp.models.historia import Historia


class historiaSerializer(serializers.ModelSerializer):

    class Meta:
        model: Historia
<<<<<<< HEAD
        fields = ['idhistoria', 'idpaciente', 'idsugerencia','encasa']
=======
        fields = ['idhistoria', 'idpaciente', 'idsugerencia','encasa']
>>>>>>> 42a80da3c8dfc441ae8e257660b0688ba657547d
