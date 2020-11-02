from employee.models import Employees
from rest_framework import serializers


class EmployeesSerializer(serializers.ModelSerializer):
    """Details of Employees"""
    class Meta:
        model = Employees
        fields = '__all__'
