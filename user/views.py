from django.shortcuts import render
from rest_framework.views import APIView
from user import serializer
from user.serializer import UserSerializer
from random import randint
from rest_framework.response import Response
from rest_framework import serializers, status
from user.models import User

# Create your views here.

class RegisterView(APIView):

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        otp = ""
        for i in range(6):
            otp = otp + str(randint(0,9))
        email = request.data['email']
        wa = request.data['wa']
        user = {
            'wa' : wa,
            'email' : email,
            'otp' : otp
        }
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        otp = ""
        for i in range(6):
            otp = otp + str(randint(0,9))
        try:
            user = User.objects.get(wa=request.data['wa'])
        except:
            return Response({"status" : "user not found"},status=status.HTTP_404_NOT_FOUND)
        myuser = {
            'wa' : request.data['wa'],
            'email' : user.email,
            'otp' : otp
        }
        
        serializer = UserSerializer(user,data = myuser)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response({'status' : 'User WA not Found'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, format=None):
        try:
            user = User.objects.get(email=request.data['email'])
        except:
            return Response({"status" : "user not found"},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
            


class LoginView(APIView):

    def get(self, request, format=None):
        user = User.objects.filter(otp=request.data['otp'])
        if user:
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'status' : 'OTP Wrong'}, status=status.HTTP_200_OK)

