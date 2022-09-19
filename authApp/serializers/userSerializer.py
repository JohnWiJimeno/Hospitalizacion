from rest_framework import serializers
from authApp.models.user import user


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model: user
        fields = ['id', 'username', 'password', 'name', 'email']