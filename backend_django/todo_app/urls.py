from django.urls import path

from rest_framework import routers
from .views import TodosViewSet


router = routers.DefaultRouter()

router.register('todos', TodosViewSet)

urlpatterns = router.urls
