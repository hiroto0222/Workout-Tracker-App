"""
Models for the core app
"""

from django.db import models


class Exercise(models.Model):
    """Exercise model

    Attributes:
        name (str): Name of the exercise
        description (str): Description of the exercise
    """

    BODY_PARTS = (
        ("Forearms", "Forearms"),
        ("Triceps", "Triceps"),
        ("Biceps", "Biceps"),
        ("Neck", "Neck"),
        ("Shoulders", "Shoulders"),
        ("Chest", "Chest"),
        ("Back", "Back"),
        ("Core", "Core"),
        ("Upper Legs", "Upper Legs"),
        ("Glutes", "Glutes"),
        ("Calves", "Calves"),
        ("Full Body", "Full Body"),
        ("Other", "Other"),
    )

    EQUIPMENT = (
        ("Barbell", "Barbell"),
        ("Dumbbell", "Dumbbell"),
        ("Machine", "Machine"),
        ("Bodyweight", "Bodyweight"),
        ("Bands", "Bands"),
        ("Cardio", "Cardio"),
        ("Other", "Other"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    body_part = models.CharField(max_length=16, choices=BODY_PARTS)
    equipment = models.CharField(max_length=16, choices=EQUIPMENT)

    def __str__(self):
        return f"Exercise(body_part={self.body_part}, equipment={self.equipment}, name={self.name}')"
