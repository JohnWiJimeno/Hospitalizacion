from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.signosvitales import Signosvitales
from authApp.serializers.signosvitalesSerializer import SignosvitalesSerializer



@api_view(['GET','POST'])
def signosvitales_api_view(request):
    if request.method == 'GET':
        signosvitales = Signosvitales.objects.all()
        signosvitales_Serializer = SignosvitalesSerializer(signosvitales,many=True)
        return Response(signosvitales_Serializer.data)

    elif request.method == 'POST':
        signosvitales_Serializer = SignosvitalesSerializer(data = request.data)
        if signosvitales_Serializer.is_valid():
            signosvitales_Serializer.save()
            return Response(signosvitales_Serializer.data)
        return Response(signosvitales_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def signosvitales_detail_view(request,pk=None):
    if request.method == 'GET':
        signosvitales=Signosvitales.objects.filter(id=pk).first()
        signosvitales_Serializer = SignosvitalesSerializer(signosvitales)
        return Response(signosvitales_Serializer.data)

    elif request.method == 'PUT':
        signosvitales=Signosvitales.objects.filter(id=pk).first()
        signosvitales_Serializer = SignosvitalesSerializer(instance=signosvitales, data = request.data)
        if signosvitales_Serializer.is_valid():
            signosvitales_Serializer.save()
            return Response(signosvitales_Serializer.data)
        return Response (signosvitales_Serializer.errors)    

    elif request.method == 'DELETE':        
        signosvitales=Signosvitales.objects.filter(id=pk).first()
        signosvitales.delete()
        return Response("Eliminado")