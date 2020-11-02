from django.urls import path, include
from .views import EmployeesViewSet


urlpatterns = [
    path('employees/', EmployeesViewSet.as_view({'get': 'list'})),
]
