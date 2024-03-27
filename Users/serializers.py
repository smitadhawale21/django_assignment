
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class VerificationSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    otp = serializers.CharField()
