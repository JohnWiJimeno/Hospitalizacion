from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models import Enfermero
from authApp.serializers import EnfermeroSerializer



@api_view(['GET','POST'])
def enfermero_api_view(request):
    if request.method == 'GET':
        enfermero = Enfermero.objects.all()
        enfermero_Serializer = EnfermeroSerializer(enfermero,many=True)
        return Response(enfermero_Serializer.data)

    elif request.method == 'POST':
        enfermero_Serializer = EnfermeroSerializer(data = request.data)
        if enfermero_Serializer.is_valid():
            enfermero_Serializer.save()
            return Response(enfermero_Serializer.data)
        return Response(enfermero_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def enfermero_detail_view(request,pk=None):
    if request.method == 'GET':
        enfermero=Enfermero.objects.filter(id=pk).first()
        enfermero_Serializer = EnfermeroSerializer(enfermero)
        return Response(enfermero_Serializer.data)

    elif request.method == 'PUT':
        enfermero=Enfermero.objects.filter(id=pk).first()
        enfermero_Serializer = EnfermeroSerializer(instance=enfermero, data = request.data)
        if enfermero_Serializer.is_valid():
            enfermero_Serializer.save()
            return Response(enfermero_Serializer.data)
        return Response (enfermero_Serializer.errors)    

    elif request.method == 'DELETE':        
        enfermero=Enfermero.objects.filter(id=pk).first()
        enfermero.delete()
        return Response("Eliminado")
