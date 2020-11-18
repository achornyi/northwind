from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import pagination
from rest_framework import viewsets
from employee.models import Employees
from employee.serializers import EmployeesSerializer


class EmployeesViewSetPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 1000


# Create your views here.
class EmployeesViewSet(viewsets.ModelViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    pagination_class = EmployeesViewSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('country', 'region', 'city', 'hire_date')
    lookup_field = 'employee_id'
    search_fields = ('first_name', 'last_name', 'title')
