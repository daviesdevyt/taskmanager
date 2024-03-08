from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import User


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse(
            "register"
        )  # replace 'register' with the actual name of your url

    def test_register_success(self):
        response = self.client.post(
            self.url, {"username": "newuser", "password": "newpass"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "User created")

    def test_register_fail(self):
        User.objects.create_user(username="existinguser", password="12345")
        response = self.client.post(
            self.url, {"username": "existinguser", "password": "newpass"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "Username already exists")


class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.url = reverse(
            "logout"
        )  # replace 'logout' with the actual name of your url

    def test_logout(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Logout successful")


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.url = reverse("login")  # replace 'login' with the actual name of your url

    def test_login_success(self):
        response = self.client.post(
            self.url, {"username": "testuser", "password": "12345"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Login successful")

    def test_login_fail(self):
        response = self.client.post(
            self.url, {"username": "wronguser", "password": "wrongpass"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "Invalid credentials")
