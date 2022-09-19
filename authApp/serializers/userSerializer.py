from rest_framework import serializers
<<<<<<< HEAD
from authApp.models.user import User 




class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email']

 
=======
from authApp.models.user import user


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model: user
        fields = ['id', 'username', 'password', 'name', 'email']
>>>>>>> 1c1cd8f73bb1a6ef8b6ec98743bacdee4c011e66
