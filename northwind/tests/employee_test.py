from django.test import TestCase
from django.test.client import Client
from employee.models import Employees
from employee.views import EmployeesViewSet


TEST_EMPLOYEE = [
        {
            "employee_id": 1,
            "territories": [
                "Wilton",
                "Neward"
            ],
            "last_name": "Davolio",
            "first_name": "Nancy",
            "title": "Sales Representative",
            "title_of_courtesy": "Ms.",
            "birth_date": "1948-12-08",
            "hire_date": "1992-05-01",
            "address": "507 - 20th Ave. E.\\nApt. 2A",
            "city": "Seattle",
            "region": "WA",
            "postal_code": "98122",
            "country": "USA",
            "home_phone": "(206) 555-9857",
            "extension": "5467",
            "photo": "",
            "notes": "Education includes a BA in psychology from Colorado State University in 1970.  She also "
                     "completed The Art of the Cold Call.  Nancy is a member of Toastmasters International.",
            "photo_path": "http://accweb/emmployees/davolio.bmp",
            "reports_to": None
        },
        {
            "employee_id": 2,
            "territories": [
                "Westboro",
                "Bedford",
                "Georgetow",
                "Boston",
                "Cambridge",
                "Braintree",
                "Louisville"
            ],
            "last_name": "Fuller",
            "first_name": "Andrew",
            "title": "Vice President, Sales",
            "title_of_courtesy": "Dr.",
            "birth_date": "1952-02-19",
            "hire_date": "1992-08-14",
            "address": "908 W. Capital Way",
            "city": "Tacoma",
            "region": "WA",
            "postal_code": "98401",
            "country": "USA",
            "home_phone": "(206) 555-9482",
            "extension": "3457",
            "photo": "",
            "notes": "Andrew received his BTS commercial in 1974 and a Ph.D. in international marketing from the "
                     "University of Dallas in 1981.  He is fluent in French and Italian and reads German.  He joined "
                     "the company as a sales representative, was promoted to sales manager in January 1992 and to "
                     "vice president of sales in March 1993.  Andrew is a member of the Sales Management Roundtable, "
                     "the Seattle Chamber of Commerce, and the Pacific Rim Importers Association.",
            "photo_path": "http://accweb/emmployees/fuller.bmp",
            "reports_to": None
        },
]


class EmployeeTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.view = EmployeesViewSet()

    def test_entries_access(self):
        response = self.c.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_employee_add(self):
        for emp in TEST_EMPLOYEE:
            Employees.objects.create(
                last_name=emp["last_name"],
                first_name=emp["first_name"],
            )
        response = self.c.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 2)
        response = self.c.post('/employees/', {'last_name': 'fake', 'first_name': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Employees.objects.count(), 3)

    def test_employee_pagination(self):
        for _ in range(15):
            Employees.objects.create(
                last_name="last_name",
                first_name="first_name",
            )
        request = self.c.get('/employees/?page=2')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 5)

