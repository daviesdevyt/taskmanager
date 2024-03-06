from django.db import models
from .choices import Status
 


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.pending
    )
    created = models.DateTimeField(auto_now_add=True)
