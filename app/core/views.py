"""
API Views for the core app.

-- exercise --
/api/exercises/ GET
/api/exercises/body_parts/ GET
/api/exercises/equipment/ GET
"""

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Exercise
from core.serializers import ExerciseSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ["get"]
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    @action(detail=False, methods=["get"])
    def body_parts(self, request):
        """return all body parts"""
        return Response(Exercise.body_part_options, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def equipment(self, request):
        """return all equipment"""
        return Response(Exercise.equipment_options, status=status.HTTP_200_OK)
