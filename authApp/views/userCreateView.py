<<<<<<< HEAD
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
=======
from rest_framework import status, views 
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

>>>>>>> 36d994949627123dfbbf025f32099bc54f8c969a
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
<<<<<<< HEAD
        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
=======

        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
                
>>>>>>> 36d994949627123dfbbf025f32099bc54f8c969a
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)