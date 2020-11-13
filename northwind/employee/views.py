from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.response import Response
from employee.models import Employees
from employee.serializers import EmployeesSerializer


class EmployeesViewSetPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 1000


# Create your views here.
class EmployeesViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    pagination_class = EmployeesViewSetPagination

    def list(self, request):
        queryset = Employees.objects.all()
        serializer = EmployeesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
