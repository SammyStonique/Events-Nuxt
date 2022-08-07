from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.reverse import reverse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUser(APIView):
    def get(self, request, format=None):
        currentuser = User.objects.filter(email=request.user)
        serializer = UserSerializer(currentuser)
        return Response(serializer.data)

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect Password!')
    
    response = Response()
    
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint, data=request.data).json()
    
    response.data = {
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
        'email': user.email
    }
    
    return response