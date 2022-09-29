from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.paciente import Paciente
from authApp.serializers.pacienteSerializer import PacienteSerializer



@api_view(['GET','POST'])
def paciente_api_view(request):
    if request.method == 'GET':
        paciente = Paciente.objects.all()
        paciente_Serializer = PacienteSerializer(paciente,many=True)
        return Response(paciente_Serializer.data)

    elif request.method == 'POST':
        paciente_Serializer = PacienteSerializer(data = request.data)
        if paciente_Serializer.is_valid():
            paciente_Serializer.save()
            return Response(paciente_Serializer.data)
        return Response(paciente_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def paciente_detail_view(request,pk=None):
    if request.method == 'GET':
        paciente=Paciente.objects.filter(id=pk).first()
        paciente_Serializer = PacienteSerializer(paciente)
        return Response(paciente_Serializer.data)

    elif request.method == 'PUT':
        paciente=Paciente.objects.filter(id=pk).first()
        paciente_Serializer = PacienteSerializer(instance=paciente, data = request.data)
        if paciente_Serializer.is_valid():
            paciente_Serializer.save()
            return Response(paciente_Serializer.data)
        return Response (paciente_Serializer.errors)    

    elif request.method == 'DELETE':        
        paciente=Paciente.objects.filter(id=pk).first()
        paciente.delete()
        return Response("Eliminado")