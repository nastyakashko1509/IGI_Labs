import logging
from django.shortcuts import render, redirect
from datetime import date
from django.contrib.auth.decorators import login_required
from information_pages.models import News, AboutCompany, PrivacyPolicy, Review, FAQ, PromoCode


logger = logging.getLogger(__name__)

@login_required
def news_list(request):
    """  Представление страницы новостей.  """

    logger.info(f"Пользователь {request.user} запросил список новостей.")
    all_news = News.objects.order_by('-published_at')
    logger.debug(f"Получено новостей: {all_news.count()}")
    return render(request, 'news_list.html', {'all_news': all_news})

@login_required
def about_company_view(request):
    """  Представление страницы с информацией о компании.  """

    logger.info(f"Пользователь {request.user} запросил информацию о компании")
    about = AboutCompany.objects.first()
    if about:
        logger.debug("Информация о компании найдена")
    else:
        logger.warning("Информация о компании не найдена")
    return render(request, 'about_company.html', {'about': about})

@login_required
def privacy_policy_view(request):
    """  Представление страницы с политикой конфиденциальности.  """

    logger.info(f"Пользователь {request.user} запросил политику конфиденциальности")
    privacy_policy = PrivacyPolicy.objects.all()
    logger.debug(f"Найдено записей политики конфиденциальности: {privacy_policy.count()}")
    return render(request, 'privacy_policy.html', {'privacy_policy': privacy_policy})

@login_required
def reviews_view(request):
    """  Представление страницы отзывов (+ crud (add)  для отзывов).  """

    if request.method == 'POST':
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        logger.info(f"Пользователь {request.user} оставляет отзыв с рейтингом {rating}")
        try:
            Review.objects.create(author=request.user, text=text, rating=int(rating))
            logger.info("Отзыв успешно создан")
        except Exception as e:
            logger.error(f"Ошибка при создании отзыва: {e}")
        return redirect('reviews')

    reviews = Review.objects.all().order_by('-created_at')
    logger.debug(f"Загружено отзывов: {reviews.count()}")
    return render(request, 'reviews.html', {'reviews': reviews})

@login_required
def faq_list(request):
    """  Представление страницы "вопрос - ответ".  """

    if request.method == 'POST':
        question_text = request.POST.get('question', '').strip()
        if question_text:
            logger.info(f"Пользователь {request.user} добавляет вопрос FAQ: {question_text}")
            try:
                FAQ.objects.create(question=question_text)
                logger.info("Вопрос успешно добавлен")
            except Exception as e:
                logger.error(f"Ошибка при добавлении вопроса FAQ: {e}")
            return redirect('faq_list')

    faqs = FAQ.objects.order_by('-added_date')
    logger.debug(f"Загружено вопросов FAQ: {faqs.count()}")
    return render(request, 'faq_list.html', {'faqs': faqs})

@login_required
def promocodes_view(request):
    """  Представление страницы с промокодами.  """

    today = date.today()
    logger.info(f"Пользователь {request.user} запросил список промокодов")
    active_codes = PromoCode.objects.filter(is_active=True, valid_until__gte=today).order_by('valid_until')
    archived_codes = PromoCode.objects.filter(is_active=False) | PromoCode.objects.filter(valid_until__lt=today)
    archived_codes = archived_codes.distinct().order_by('-valid_until')
    logger.debug(f"Активных промокодов: {active_codes.count()}, Архивных: {archived_codes.count()}")

    return render(request, 'promocodes.html', {
        'active_codes': active_codes,
        'archived_codes': archived_codes,
    })
