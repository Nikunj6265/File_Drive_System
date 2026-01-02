from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "Registered successfully"})
    

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })

class Folder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "owner")

    def __str__(self):
        return self.name
