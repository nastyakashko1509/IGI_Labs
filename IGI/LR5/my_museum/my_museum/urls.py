from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path, path
from authentication.views import home, register, register_employee, register_client, RoleBasedLoginView
from museum.views import vacancies_view, museum_info, programming_joke, employee_list, main, employee_detail, employee_dashboard, client_dashboard, admin_dashboard
from museum.views_statistics.statistics import statistics_view
from museum.views_graphic.statistics_graphs import sales_charts_page, sales_by_visitor_age_chart, sales_by_day_type_chart, sales_over_time_chart
from information_pages.views import news_list, about_company_view, privacy_policy_view, reviews_view, faq_list, promocodes_view
from  museum.views_crud.crud_employee import index, employee_create, employee_edit, employee_delete
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    re_path(r'^$', home, name='home'),
    re_path(r'^main/$', main, name='main'),

    re_path(r'^login/$', RoleBasedLoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^register-employee/$', register_employee, name='register_employee'),
    re_path(r'^register_client/$', register_client, name='register_client'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

    re_path(r'^museum_info/$', museum_info, name='museum_info'),
    re_path(r'^joke/$', programming_joke, name='joke'),

    re_path(r'^employee/$', employee_list, name='employee'),
    re_path(r'^employee_dashboard/$', employee_dashboard, name='employee_dashboard'),
    re_path(r'^employee/(?P<employee_id>\d+)/$', employee_detail, name='employee_detail'),
    re_path(r'^client_dashboard/$', client_dashboard, name='client_dashboard'),
    re_path(r'^news/$', news_list, name='news_list'),
    re_path(r'^vacancies/$', vacancies_view, name='vacancies'),
    re_path(r'^about/$', about_company_view, name='about'),
    re_path(r'^privacy_policy/$', privacy_policy_view, name='privacy_policy'),
    re_path(r'^reviews/$', reviews_view, name='reviews'),
    re_path(r'^faq/$', faq_list, name='faq_list'),
    re_path(r'^promocodes/$', promocodes_view, name='promocodes'),

    re_path(r'^statistics/$', statistics_view, name='statistics'),

    path('charts/age/', sales_by_visitor_age_chart, name='sales_by_age_chart'),
    path('charts/daytype/', sales_by_day_type_chart, name='sales_by_day_type_chart'),
    path('charts/overtime/', sales_over_time_chart, name='sales_over_time_chart'),
    path('charts/', sales_charts_page, name='sales_charts_page'),

    path('employees/', index, name='employee_list'),
    path('employees/create/', employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', employee_edit, name='employee_edit'),
    path('employees/<int:pk>/delete/', employee_delete, name='employee_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
