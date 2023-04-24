"""
Serializers for core app.
"""

from rest_framework import serializers

from core.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
