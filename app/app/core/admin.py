"""
Admin configuration for core app
"""

from core.models import Exercise
from django.contrib import admin


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "body_part",
        "name",
        "equipment",
        "description",
    )


admin.site.register(Exercise, ExerciseAdmin)
