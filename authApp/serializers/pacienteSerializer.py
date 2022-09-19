from rest_framework import serializers
from authApp.models.paciente import paciente


class pacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model: paciente
        fields = ['idpaciente', 'nombre', 'apellidos','ciudad', 'direccion', 
        'fechanacimiento', 'latitud', 'longitud', 'email', 'idfamiliar', 'idmedico',
        'idenfermero', 'idauxiliar', 'user']