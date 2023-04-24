"""
Admin configuration for core app.
"""

from django.contrib import admin

from core.models import Exercise


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "body_part",
        "name",
        "equipment",
        "description",
    )


admin.site.register(Exercise, ExerciseAdmin)
