"""
URLS for core API
"""

from rest_framework.routers import SimpleRouter

from core.views import ExerciseViewSet

core_router = SimpleRouter()

core_router.register(r"exercise", ExerciseViewSet, basename="exercise")
