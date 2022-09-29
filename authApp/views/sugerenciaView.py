from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.sugerencia import Sugerencia
from authApp.serializers.sugerenciaSerializer import SugerenciaSerializer



@api_view(['GET','POST'])
def sugerencia_api_view(request):
    if request.method == 'GET':
        sugerencia = Sugerencia.objects.all()
        sugerencia_Serializer = SugerenciaSerializer(sugerencia,many=True)
        return Response(sugerencia_Serializer.data)

    elif request.method == 'POST':
        sugerencia_Serializer = SugerenciaSerializer(data = request.data)
        if sugerencia_Serializer.is_valid():
            sugerencia_Serializer.save()
            return Response(sugerencia_Serializer.data)
        return Response(sugerencia_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def sugerencia_detail_view(request,pk=None):
    if request.method == 'GET':
        sugerencia=Sugerencia.objects.filter(id=pk).first()
        sugerencia_Serializer = SugerenciaSerializer(sugerencia)
        return Response(sugerencia_Serializer.data)

    elif request.method == 'PUT':
        sugerencia=Sugerencia.objects.filter(id=pk).first()
        sugerencia_Serializer = SugerenciaSerializer(instance=sugerencia, data = request.data)
        if sugerencia_Serializer.is_valid():
            sugerencia_Serializer.save()
            return Response(sugerencia_Serializer.data)
        return Response (sugerencia_Serializer.errors)    

    elif request.method == 'DELETE':        
        sugerencia=Sugerencia.objects.filter(id=pk).first()
        sugerencia.delete()
        return Response("Eliminado")