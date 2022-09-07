"""
Serializers for Custom Users 
"""

from rest_framework import serializers
from .models import CustomUser


class SignUpSerializers(serializers.ModelSerializer):
    """create new user serializers"""
    class Meta:
        model = CustomUser
        fields = ['username','password']

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        return CustomUser.objects.create_user(username,password)

class LoginSerializer(serializers.ModelSerializer):
    """login serializer using CustomUser model"""

    class Meta:
        model = CustomUser
        fields = ['username','password']

class ListUserSerilier(serializers.ModelSerializer):
    """List all users with their role"""

    class Meta:
        model = CustomUser
        fields = ['username','is_staff','is_superuser']