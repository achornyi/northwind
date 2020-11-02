from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.response import Response
from employee.models import Employees
from employee.serializers import EmployeesSerializer


# Create your views here.
class EmployeesViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        queryset = Employees.objects.all()
        serializer = EmployeesSerializer(queryset, many=True)
        pagination.PageNumberPagination.page_size = 5
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
