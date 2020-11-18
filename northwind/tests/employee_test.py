from unittest.mock import patch, ANY

from rest_framework.test import APITestCase

from employee.models import Employees
from employee.views import EmployeesViewSetPagination


class EmployeeTest(APITestCase):
    def setUp(self) -> None:
        self.employee_john = Employees.objects.create(
            last_name="John", first_name="Doe",
        )
        self.employee_jane = Employees.objects.create(
            last_name="Jane", first_name="Doe",
        )

    def test_list(self):
        response = self.client.get("/employees/")
        self.assertEqual(response.status_code, 200)
        results_ = response.json()["results"]
        self.assertEqual(
            len(results_), 2,
        )
        self.assertGreaterEqual(
            results_[0].items(),
            {
                "employee_id": self.employee_john.employee_id,
                "last_name": "John",
                "first_name": "Doe",
            }.items(),
        )
        self.assertGreaterEqual(
            results_[1].items(),
            {
                "employee_id": self.employee_jane.employee_id,
                "last_name": "Jane",
                "first_name": "Doe",
            }.items(),
        )

    def test_details(self):
        response = self.client.get(
            "/employees/{employee_id}/".format(
                employee_id=self.employee_john.employee_id
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "employee_id": self.employee_john.employee_id,
                "territories": [],
                "last_name": "John",
                "first_name": "Doe",
                "title": None,
                "title_of_courtesy": None,
                "birth_date": None,
                "hire_date": None,
                "address": None,
                "city": None,
                "region": None,
                "postal_code": None,
                "country": None,
                "home_phone": None,
                "extension": None,
                "photo": None,
                "notes": None,
                "photo_path": None,
                "reports_to": None,
            },
        )

    def test_create(self):
        response = self.client.post(
            "/employees/", {"last_name": "fake", "first_name": "test"}
        )
        self.assertEqual(response.status_code, 201)
        created_instance = Employees.objects.get(
            employee_id=response.json()["employee_id"]
        )
        self.assertEqual(created_instance.first_name, "test")
        self.assertEqual(created_instance.last_name, "fake")

    @patch.object(EmployeesViewSetPagination, "page_size", 1)
    def test_pagination(self):
        response = self.client.get("/employees/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "count": 2,
                "next": "http://testserver/employees/?page=2",
                "previous": None,
                "results": [ANY],  # one result
            },
        )
