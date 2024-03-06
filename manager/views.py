from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

# Create your views here.
from .models import Task
from .serializer import TaskSerializer

class TaskView(
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
):
    model = Task
    serializer_class = TaskSerializer
