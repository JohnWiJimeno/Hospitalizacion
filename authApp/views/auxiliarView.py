from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.auxiliar import Auxiliar
from authApp.serializers.auxiliarSerializer import AuxiliarSerializer



@api_view(['GET','POST'])
def auxiliar_api_view(request):
    if request.method == 'GET':
        auxiliar = Auxiliar.objects.all()
        auxiliar_Serializer = AuxiliarSerializer(auxiliar,many=True)
        return Response(auxiliar_Serializer.data)

    elif request.method == 'POST':
        auxiliar_Serializer = AuxiliarSerializer(data = request.data)
        if auxiliar_Serializer.is_valid():
            auxiliar_Serializer.save()
            return Response(auxiliar_Serializer.data)
        return Response(auxiliar_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def auxiliar_detail_view(request,pk=None):
    if request.method == 'GET':
        auxiliar=Auxiliar.objects.filter(id=pk).first()
        auxiliar_Serializer = AuxiliarSerializer(auxiliar)
        return Response(auxiliar_Serializer.data)

    elif request.method == 'PUT':
        auxiliar=Auxiliar.objects.filter(id=pk).first()
        auxiliar_Serializer = AuxiliarSerializer(instance=auxiliar, data = request.data)
        if auxiliar_Serializer.is_valid():
            auxiliar_Serializer.save()
            return Response(auxiliar_Serializer.data)
        return Response (auxiliar_Serializer.errors)    

    elif request.method == 'DELETE':        
        auxiliar=Auxiliar.objects.filter(id=pk).first()
        auxiliar.delete()
        return Response("Eliminado")
