from django.contrib import admin
from .models import Class, Activity


class ClassAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)
  ordering = ('name',)
  readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Class, ClassAdmin)


class ActivityAdmin(admin.ModelAdmin):
  list_display = ('description',)
  search_fields = ('description',)
  ordering = ('description',)
  readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Activity, ActivityAdmin)
