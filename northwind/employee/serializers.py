from employee.models import Employees
from rest_framework import serializers


class EmployeesSerializer(serializers.ModelSerializer):
    """Details of Employees"""
    territories = serializers.SlugRelatedField(slug_field='territory_description', read_only=True, many=True)

    class Meta:
        model = Employees
        fields = '__all__'
