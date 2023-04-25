"""
Models for the core app.
"""

from typing import List

from django.db import models
from django.utils.functional import classproperty


class Exercise(models.Model):
    """Exercise object"""

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
    equipment = models.CharField(max_length=16, choices=EQUIPMENT)
    body_part = models.CharField(max_length=16, choices=BODY_PARTS)

    @classproperty
    def body_part_options(self) -> List[str]:
        return [x[0] for x in self.BODY_PARTS]

    @classproperty
    def equipment_options(self) -> List[str]:
        return [x[0] for x in self.EQUIPMENT]

    def __str__(self):
        return self.name
