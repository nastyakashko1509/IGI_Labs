from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from museum.models.Employee import Employee
from django.core.files.storage import FileSystemStorage
from museum.models.Position import Position
from museum.models.Hall import Hall
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from museum.models.Client import Client
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

def home(request):
    """  Представление главной страницы.  """

    logger.info("Запрос к главной странице (home.html).")
    return render(request, 'home.html')

def register(request):
    """  Регистрация user (без роли) - crud операция (add).  """

    logger.info("Запрос на регистрацию без роли.")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def register_employee(request):
    """  Регистрация user (с ролью "сотрудник") - crud операция (add).  """

    logger.info("Запрос на регистрацию в роли сотрудника.")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        position_id = request.POST.get('position')
        hall_ids = request.POST.getlist('halls')
        work_description = request.POST.get('work_description')
        photo = request.FILES.get('photo')
        date_of_birth = request.POST.get('date_of_birth')

        form_values = {
            'username': username,
            'email': email,
            'full_name': full_name,
            'phone': phone,
            'bio': bio,
            'position': position_id,
            'work_description': work_description,
            'halls': hall_ids,
            'date_of_birth': date_of_birth,
        }

        if not (username and password and full_name):
            return render(request, 'register_employee.html', {
                'error': 'Обязательные поля не заполнены!',
                'positions': Position.objects.all(),
                'halls': Hall.objects.all(),
                'form_values': form_values,
                'selected_halls': hall_ids,
            })

        user = User.objects.create_user(username=username, password=password, email=email)

        photo_path = None
        if photo:
            fs = FileSystemStorage()
            photo_path = fs.save(f'photos/employees/{photo.name}', photo)

        employee = Employee.objects.create(
            user=user,
            full_name=full_name,
            phone=phone,
            email=email,
            bio=bio,
            date_of_birth=date_of_birth,
            work_description=work_description,
            photo=photo_path,
            position_id=position_id
        )

        try:
            employee.full_clean()  
        except ValidationError as e:
            logger.error(f"Ошибка в полях регистрации: {e}.")
            user.delete()
            return render(request, 'register_employee.html', {
                'error': e.message_dict,
                'positions': Position.objects.all(),
                'halls': Hall.objects.all(),
                'form_values': form_values,
            })
        employee.save()

        if hall_ids:
            employee.halls.set(hall_ids)

        return redirect('login')

    context = {
        'positions': Position.objects.all(),
        'halls': Hall.objects.all()
    }
    return render(request, 'register_employee.html', context)

def register_client(request):
    """  Регистрация user (с ролью "клиент") - crud операция (add).  """

    logger.info("Запрос на регистрацию в роли клиента.")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')

        form_values = {
            'username': username,
            'email': email,
            'full_name': full_name,
            'date_of_birth': date_of_birth,
            'phone_number': phone_number
        }

        if not (username and password and full_name and date_of_birth):
            return render(request, 'register_client.html', {
                'error': 'Обязательные поля не заполнены!',
                'form_values': form_values,
            })

        user = User.objects.create_user(username=username, password=password, email=email)

        client = Client(
            user=user,
            full_name=full_name,
            email=email,
            date_of_birth=date_of_birth,
            phone_number=phone_number
        )

        try:
            client.full_clean()
            client.save()
        except ValidationError as e:
            logger.error(f"Ошибка в полях при регистрации: {e}.")
            user.delete()
            return render(request, 'register_client.html', {
                'error': e.message_dict,
                'form_values': form_values,
            })

        return redirect('login')

    return render(request, 'register_client.html')

class RoleBasedLoginView(LoginView):
    """  Перенаправление после входа: клиент на страницу клиента, админа - админа, сотрудник - сотрудника.  """

    logger.info("Перенаправление после входа на страницы сотрудника/клиента/админа.")
    def get_success_url(self):
        user = self.request.user
        
        if user.is_superuser:
            return reverse('admin_dashboard') 
        
        if hasattr(user, 'museum_employee'):
            return reverse('employee_dashboard') 
        
        if hasattr(user, 'museum_client'):
            return reverse('client_dashboard') 

        return reverse('main')
