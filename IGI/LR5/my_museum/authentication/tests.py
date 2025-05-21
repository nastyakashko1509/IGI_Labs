from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from museum.models import Position, Hall
from django.core.files.uploadedfile import SimpleUploadedFile


class AuthenticationViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(title='Экскурсовод')
        self.hall1 = Hall.objects.create(name='История', floor=1)
        self.hall2 = Hall.objects.create(name='Наука', floor=2)

    def test_home_view(self):
        """  Тест главной страницы (home view) на корректный статус и шаблон.  """

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_register_view_get(self):
        """  Тест GET-запроса страницы регистрации (register view).  """

        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post(self):
        """  Тест POST-запроса регистрации нового пользователя (register view).  """

        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'Testpass123',
            'password2': 'Testpass123',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_client_view_post(self):
        """  Тест регистрации клиента через register_client view.  """

        response = self.client.post(reverse('register_client'), {
            'username': 'client1',
            'password': 'Testpass123',
            'email': 'client@test.com',
            'full_name': 'Клиент Тестовый',
            'date_of_birth': '1990-01-01'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='client1').exists())

    def test_register_employee_view_post(self):
        """  Тест регистрации сотрудника через register_employee view с загрузкой фотографии и выбором залов.  """

        photo = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('register_employee'), {
            'username': 'employee1',
            'password': 'Testpass123',
            'email': 'employee@test.com',
            'full_name': 'Сотрудник Тестовый',
            'phone': '+375 (29) 789-98-96',
            'bio': 'Биография сотрудника',
            'position': self.position.id,
            'work_description': 'Описание работы',
            'photo': photo,
            'halls': [self.hall1.id, self.hall2.id],
            'date_of_birth': '1985-05-05'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='employee1').exists())

    def test_login_redirects_by_role(self):
        """  Тест перенаправления после входа в систему в зависимости от роли (на пример администратора).  """
        
        admin = User.objects.create_superuser(username='admin', password='adminpass', email='admin@test.com')
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'adminpass'}, follow=True)
        self.assertRedirects(response, reverse('admin_dashboard'))
