from django.db import models
from utils.models import BaseModel


class Class(BaseModel):
  name = models.CharField (
    max_length=255,
    help_text='Name of the class',
    verbose_name='Class Name'
  )
  # teacher to implements
  def __str__(self):
    return self.name
  class Meta:
    verbose_name = 'Class'
    verbose_name_plural = 'Classes'


class Activity(BaseModel):
  description = models.TextField (
    help_text='Description of the activity',
    verbose_name='Activity Description'
  )
  class_id = models.ForeignKey (
    Class,
    on_delete=models.PROTECT,
    related_name='activities',
    help_text='Class of the activity',
    verbose_name='Class'
  )
  class Meta:
    verbose_name = 'Activity'
    verbose_name_plural = 'Activities'
