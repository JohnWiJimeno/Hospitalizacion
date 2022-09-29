from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.detallesignos import Detallesignos
from authApp.serializers.detallesignosSerializer import DetallesignosSerializer



@api_view(['GET','POST'])
def detallesignos_api_view(request):
    if request.method == 'GET':
        detallesignos = Detallesignos.objects.all()
        detallesignos_Serializer = DetallesignosSerializer(detallesignos,many=True)
        return Response(detallesignos_Serializer.data)

    elif request.method == 'POST':
        detallesignos_Serializer = DetallesignosSerializer(data = request.data)
        if detallesignos_Serializer.is_valid():
            detallesignos_Serializer.save()
            return Response(detallesignos_Serializer.data)
        return Response(detallesignos_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def detallesignos_detail_view(request,pk=None):
    if request.method == 'GET':
        detallesignos=Detallesignos.objects.filter(id=pk).first()
        detallesignos_Serializer = DetallesignosSerializer(detallesignos)
        return Response(detallesignos_Serializer.data)

    elif request.method == 'PUT':
        detallesignos=Detallesignos.objects.filter(id=pk).first()
        detallesignos_Serializer = DetallesignosSerializer(instance=detallesignos, data = request.data)
        if detallesignos_Serializer.is_valid():
            detallesignos_Serializer.save()
            return Response(detallesignos_Serializer.data)
        return Response (detallesignos_Serializer.errors)    

    elif request.method == 'DELETE':        
        detallesignos=Detallesignos.objects.filter(id=pk).first()
        detallesignos.delete()
        return Response("Eliminado")