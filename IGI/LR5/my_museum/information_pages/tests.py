from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta
from information_pages.models import News, AboutCompany, PrivacyPolicy, Review, FAQ, PromoCode


class InformationPagesViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        self.client.login(username='testuser', password='password123')

        News.objects.create(title="Новость 1", published_at=date.today())
        AboutCompany.objects.create(content="О компании")
        PrivacyPolicy.objects.create()
        Review.objects.create(author=self.user, text="Отзыв", rating=5)
        FAQ.objects.create(question="Вопрос?")
        PromoCode.objects.create(code="PROMO1", is_active=True, valid_until=date.today() + timedelta(days=5))
        PromoCode.objects.create(code="PROMO2", is_active=False, valid_until=date.today() - timedelta(days=5))

    def test_news_list(self):
        """  Проверка загрузки списка новостей.  """
        
        url = reverse('news_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('all_news', response.context)
        self.assertGreater(len(response.context['all_news']), 0)

    def test_about_company_view(self):
        """  Проверка страницы 'О компании'.  """

        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('about', response.context)
        self.assertIsNotNone(response.context['about'])

    def test_privacy_policy_view(self):
        """  Проверка страницы политики конфиденциальности.  """

        url = reverse('privacy_policy')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('privacy_policy', response.context)
        self.assertGreater(len(response.context['privacy_policy']), 0)

    def test_reviews_view_get(self):
        """  Проверка загрузки страницы отзывов (GET-запрос).  """

        url = reverse('reviews')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('reviews', response.context)

    def test_reviews_view_post(self):
        """  Проверка добавления отзыва (POST-запрос).  """

        url = reverse('reviews')
        response = self.client.post(url, data={'rating': '4', 'text': 'Хороший отзыв'})
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Review.objects.filter(text='Хороший отзыв', rating=4, author=self.user).exists())

    def test_faq_list_get(self):
        """  Проверка загрузки списка часто задаваемых вопросов (GET-запрос).  """

        url = reverse('faq_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('faqs', response.context)

    def test_faq_list_post(self):
        """  Проверка добавления нового вопроса (POST-запрос).  """

        url = reverse('faq_list')
        response = self.client.post(url, data={'question': 'Новый вопрос?'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FAQ.objects.filter(question='Новый вопрос?').exists())

    def test_promocodes_view(self):
        """  Проверка отображения активных и неактивных промокодов.  """

        url = reverse('promocodes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('active_codes', response.context)
        self.assertIn('archived_codes', response.context)
        self.assertGreater(len(response.context['active_codes']), 0)
        self.assertGreater(len(response.context['archived_codes']), 0)

    def test_login_required_redirect(self):
        """  Проверка, что для доступа к страницам требуется авторизация.  """

        self.client.logout()
        urls = [
            reverse('news_list'),
            reverse('about'),
            reverse('privacy_policy'),
            reverse('reviews'),
            reverse('faq_list'),
            reverse('promocodes'),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login', response.url)
