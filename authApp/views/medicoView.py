from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.medico import Medico
from authApp.serializers.medicoSerializer import MedicoSerializer



@api_view(['GET','POST'])
def medico_api_view(request):
    if request.method == 'GET':
        medico = Medico.objects.all()
        medico_Serializer = MedicoSerializer(medico,many=True)
        return Response(medico_Serializer.data)

    elif request.method == 'POST':
        medico_Serializer = MedicoSerializer(data = request.data)
        if medico_Serializer.is_valid():
            medico_Serializer.save()
            return Response(medico_Serializer.data)
        return Response(medico_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def medico_detail_view(request,pk=None):
    if request.method == 'GET':
        medico=Familiar.objects.filter(id=pk).first()
        medico_Serializer = MedicoSerializer(medico)
        return Response(medico_Serializer.data)

    elif request.method == 'PUT':
        medico=Medico.objects.filter(id=pk).first()
        medico_Serializer = MedicoSerializer(instance=medico, data = request.data)
        if medico_Serializer.is_valid():
            medico_Serializer.save()
            return Response(medico_Serializer.data)
        return Response (medico_Serializer.errors)    

    elif request.method == 'DELETE':        
        medico=Medico.objects.filter(id=pk).first()
        medico.delete()
        return Response("Eliminado")