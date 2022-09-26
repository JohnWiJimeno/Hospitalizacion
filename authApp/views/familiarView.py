from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authApp.models.familiar import Familiar
from authApp.serializers.familiarSerializer import FamiliarSerializer



@api_view(['GET','POST'])
def familiar_api_view(request):
    if request.method == 'GET':
        familiar = Familiar.objects.all()
        familiar_Serializer = FamiliarSerializer(familiar,many=True)
        return Response(familiar_Serializer.data)

    elif request.method == 'POST':
        familiar_Serializer = FamiliarSerializer(data = request.data)
        if familiar_Serializer.is_valid():
            familiar_Serializer.save()
            return Response(familiar_Serializer.data)
        return Response(familiar_Serializer.errors)   

@api_view(['GET','PUT','DELETE'])
def familiar_detail_view(request,pk=None):
    if request.method == 'GET':
        familiar=Familiar.objects.filter(id=pk).first()
        familiar_Serializer = FamiliarSerializer(familiar)
        return Response(familiar_Serializer.data)

    elif request.method == 'PUT':
        familiar=Familiar.objects.filter(id=pk).first()
        familiar_Serializer = FamiliarSerializer(instance=familiar, data = request.data)
        if familiar_Serializer.is_valid():
            familiar_Serializer.save()
            return Response(familiar_Serializer.data)
        return Response (familiar_Serializer.errors)    

    elif request.method == 'DELETE':        
        familiar=Familiar.objects.filter(id=pk).first()
        familiar.delete()
        return Response("Eliminado")