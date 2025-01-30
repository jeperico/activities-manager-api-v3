from management import api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'class', api.ClassViewSet)
router.register(r'activity', api.ActivityViewSet)
router.register(r'class', api.ClassRegister, basename='register-class')
router.register(r'activity', api.ActivityRegister, basename='register-activity')

urlpatterns = [
  path('', include(router.urls)),
]
