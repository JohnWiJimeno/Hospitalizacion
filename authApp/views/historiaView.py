from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.historia import Historiaclinica
from authApp.serializers.historiaSerializer import HistoriaSerializer



@api_view(['GET','POST'])
def historia_api_view(request):
    if request.method == 'GET':
        historia = Historiaclinica.objects.all()
        historia_Serializer = HistoriaSerializer(historia,many=True)
        return Response(historia_Serializer.data)

    elif request.method == 'POST':
        historia_Serializer = HistoriaSerializer(data = request.data)
        if historia_Serializer.is_valid():
            historia_Serializer.save()
            return Response(historia_Serializer.data)
        return Response(historia_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def historia_detail_view(request,pk=None):
    if request.method == 'GET':
        historia=Historia.objects.filter(id=pk).first()
        historia_Serializer = HistoriaSerializer(historia)
        return Response(historia_Serializer.data)

    elif request.method == 'PUT':
        historia=Historia.objects.filter(id=pk).first()
        historia_Serializer = HistoriaSerializer(instance=historia, data = request.data)
        if historia_Serializer.is_valid():
            historia_Serializer.save()
            return Response(historia_Serializer.data)
        return Response (historia_Serializer.errors)    

    elif request.method == 'DELETE':        
        historia=Historia.objects.filter(id=pk).first()
        historia.delete()
        return Response("Eliminado")