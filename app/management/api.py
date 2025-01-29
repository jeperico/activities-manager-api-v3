from .models import Class, Activity
from .serializers import (
  ClassReadSerializer,
  ClassRegisterSerializer,
  ActivityReadSerializer,
  ActivityRegisterSerializer,
)
from rest_framework import (
  mixins,
  viewsets,
)


class ClassViewSet(viewsets.GenericViewSet):
  queryset = Class.objects.all()
  serializer_class = ClassReadSerializer
  search_fields = ['name']


class ClassRegister(
  mixins.CreateModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Class.objects.all()
  serializer_class = ClassRegisterSerializer
  
  def perform_create(self, serializer):
    return super().perform_create(serializer)


class ActivityViewSet(viewsets.GenericViewSet):
  queryset = Activity.objects.all()
  serializer_class = ActivityReadSerializer
  search_fields = ['description']


class ActivityRegister(
  mixins.CreateModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Activity.objects.all()
  serializer_class = ActivityRegisterSerializer
  
  def perform_create(self, serializer):
    return super().perform_create(serializer)
