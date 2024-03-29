from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import RegisterSerializer, LoginSerializer


# Create your views here.
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists"}, status=400)
        User.objects.create_user(username=username, password=password)
        return Response({"message": "User created"}, status=201)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"})
        else:
            return Response({"message": "Invalid credentials"}, status=400)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({"message": "Logout successful"})
