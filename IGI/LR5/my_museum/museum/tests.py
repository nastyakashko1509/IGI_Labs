from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from museum.models import Employee, Hall, Exhibition, Exposition
from datetime import datetime, timedelta
import pytz
from datetime import date


class MuseumViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.employee = Employee.objects.create(user=self.user, full_name="Иван Иванов", date_of_birth=date(1990, 1, 1))
        self.client.login(username="testuser", password="testpass")

    def test_museum_info_access(self):
        """  Тест доступности страницы museum_info без авторизации.  """

        self.client.logout()
        response = self.client.get(reverse('museum_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'museum_info.html')

    def test_programming_joke_authenticated(self):
        """  Тест загрузки страницы с шутками.  """

        response = self.client.get(reverse('joke'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("joke", response.context)

    def test_employee_list_filter_by_age(self):
        """  Тест фильтрации сотрудников по возрасту.  """

        response = self.client.get(reverse('employee'), {'age': '35'})  # возраст 1990 -> 2025 - 1990
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Иван Иванов")

    def test_employee_detail_view(self):
        """  Тест детального представления сотрудника.  """

        response = self.client.get(reverse('employee_detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Иван Иванов")

    def test_admin_dashboard_season_tours(self):
        """  Тест отображения количества посетителей в сезон.  """

        exposition = Exposition.objects.create(name="Тестовая экспозиция", description="Тест")
        hall = Hall.objects.create(name="Main Hall", floor=1)

        Exhibition.objects.create(
            title="Test Expo",
            start_date=datetime.now(pytz.UTC) + timedelta(days=10),
            end_date=datetime.now(pytz.UTC) + timedelta(days=20),
            exposition=exposition,
            hall=hall
        )
        response = self.client.get(reverse('admin_dashboard'), {'season': 'лето'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("exhibits", response.context)
