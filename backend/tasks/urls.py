from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, TaskListViewSet

router = DefaultRouter()
router.register(r"item", ItemViewSet)
router.register(r"tasklist", TaskListViewSet)

urlpatterns = [
    path("", include(router.urls))
]
