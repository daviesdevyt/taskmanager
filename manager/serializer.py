from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "status", "created"]

