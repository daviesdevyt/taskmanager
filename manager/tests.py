from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer
from user.models import User

class TaskViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(user=self.user, title='Test Task', description='Test Description')
        self.url = "/api/tasks/"

    def test_task_list(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_create(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.url, {'title': 'New Task', 'description': 'New Description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.patch(f"/api/task/{self.task.id}/", {'title': 'Updated Task', 'status': 'completed'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_delete(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.delete(f"/api/task/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)