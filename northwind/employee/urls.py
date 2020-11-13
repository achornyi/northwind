from django.urls import path, include
from .views import EmployeesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeesViewSet, basename='employees')
urlpatterns = router.urls
