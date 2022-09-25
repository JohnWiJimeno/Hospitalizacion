from rest_framework import serializers
from authApp.models.paciente import Paciente


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model: Paciente
        fields = ['idpaciente', 'nombre', 'apellidos','ciudad', 'direccion', 
        'fechanacimiento', 'latitud', 'longitud', 'email', 'idfamiliar', 'idmedico',
        'idenfermero', 'idauxiliar', 'user']
