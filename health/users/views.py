# users/views.py
from rest_framework import generics

from . import models
from . import serializers
from django.shortcuts import render

# Create your views here.

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
