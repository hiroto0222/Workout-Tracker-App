"""
Tests for core API
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Exercise
from core.serializers import ExerciseSerializer

EXERCISES_URL = reverse("api:exercise-list")


class PublicExerciseApiTests(TestCase):
    """Test the publicly available exercises API"""

    def setUp(self):
        """Setup unauthorized client"""
        self.client = APIClient()

    def test_get_exercises(self):
        """Test retrieving exercises"""
        res = self.client.get(EXERCISES_URL)

        exercises = Exercise.objects.all().order_by("-id")
        serializer = ExerciseSerializer(exercises, many=True)

        self.assertEqual(res.data, serializer.data)  # type: ignore
        self.assertEqual(res.status_code, status.HTTP_200_OK)
