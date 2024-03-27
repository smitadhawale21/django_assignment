
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from .serializers import UserSerializer, VerificationSerializer
from django.core.mail import send_mail
from django.conf import settings
import random

@api_view(['POST'])
def registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verification(request):
    serializer = VerificationSerializer(data=request.data)
    if serializer.is_valid():
        email_or_username = serializer.validated_data['email_or_username']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email_or_username)
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=email_or_username)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        # Your OTP verification logic here
        if otp == "1234":  # Replace "1234" with your actual OTP verification logic
            return Response("Verification successful", status=status.HTTP_200_OK)
        else:
            return Response("Invalid OTP", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = VerificationSerializer(data=request.data)
    if serializer.is_valid():
        email_or_username = serializer.validated_data['email_or_username']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email_or_username)
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=email_or_username)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        # Your login logic here
        if otp == "1234":  # Replace "1234" with your actual login logic
            return Response("Login successful", status=status.HTTP_200_OK)
        else:
            return Response("Invalid OTP", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def forgot_password(request):
    serializer = VerificationSerializer(data=request.data)
    if serializer.is_valid():
        email_or_username = serializer.validated_data['email_or_username']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email_or_username)
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=email_or_username)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        # Your forgot password logic here
        if otp == "1234":  # Replace "1234" with your actual forgot password logic
            return Response("Password reset OTP sent", status=status.HTTP_200_OK)
        else:
            return Response("Invalid OTP", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reset_password(request):
    serializer = VerificationSerializer(data=request.data)
    if serializer.is_valid():
        email_or_username = serializer.validated_data['email_or_username']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email_or_username)
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=email_or_username)
            except ObjectDoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        # Your reset password logic here
        if otp == "1234":  # Replace "1234" with your actual reset password logic
            return Response("Password reset successful", status=status.HTTP_200_OK)
        else:
            return Response("Invalid OTP", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
