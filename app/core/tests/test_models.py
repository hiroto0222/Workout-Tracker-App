"""
Tests for core.models
"""

from core import models
from django.test import TestCase


class ModelTests(TestCase):
    """Test core.models"""

    def test_create_exercise(self):
        """Test creating an exercise is successful"""
        exercise = models.Exercise.objects.create(
            name="Bench Press",
            description="Lay on bench and press barbell",
            equipment="Barbell",
            body_part="Chest",
        )
        self.assertEqual(str(exercise), exercise.name)
