from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .models import Task
from .serializer import TaskSerializer


class TaskView(ListAPIView, CreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("-created")

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class TaskEditView(UpdateAPIView, DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    model = Task
    serializer_class = TaskSerializer
    lookup_field = "id"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

