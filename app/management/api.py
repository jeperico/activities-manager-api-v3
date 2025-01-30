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


class ClassViewSet(
  mixins.ListModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Class.objects.all()
  serializer_class = ClassReadSerializer
  search_fields = ['name']


class ClassRegister(
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Class.objects.all()
  serializer_class = ClassRegisterSerializer
  
  def perform_create(self, serializer):
    return super().perform_create(serializer)
  
  def update(self, request, *args, **kwargs):
    return super().update(request, *args, **kwargs)
  
  def retrieve(self, request, *args, **kwargs):
    instance = Class.objects.get(id=request.id)
    serializer = ClassReadSerializer(instance)
    return Response(serializer.data)


class ActivityViewSet(
  mixins.ListModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Activity.objects.all()
  serializer_class = ActivityReadSerializer
  search_fields = ['description']


class ActivityRegister(
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Activity.objects.all()
  serializer_class = ActivityRegisterSerializer
  
  def perform_create(self, serializer):
    return super().perform_create(serializer)
  
  def update(self, request, *args, **kwargs):
    return super().update(request, *args, **kwargs)
  
  def retrieve(self, request, *args, **kwargs):
    instance = Activity.objects.get(id=request.id)
    serializer = ActivityReadSerializer(instance)
    return Response(serializer.data)
