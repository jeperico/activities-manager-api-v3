from .models import Class, Activity
from rest_framework import serializers


class ClassReadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    fields = ['id', 'name', 'created_at', 'updated_at']


class ClassRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    fields = ['name']

  def create(self, validated_data):
    return Class.objects.create(**validated_data)


class ActivityReadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = ['id', 'description', 'class_id', 'created_at', 'updated_at']


class ActivityRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = ['description', 'class_id']

  def create(self, validated_data):
    return Activity.objects.create(**validated_data)
