from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User as AdmUser
from museum.models import Position, Hall, Employee
from django.core.exceptions import ValidationError
from museum.forms import EmployeeForm
from django.contrib import messages 


employee_not_found = "<h2>Employee not found</h2>"

def index(request):
    employees = Employee.objects.select_related('user', 'position').prefetch_related('halls').all()
    positions = Position.objects.all()
    halls = Hall.objects.all()
    users = AdmUser.objects.all()

    return render(request, "crud_employee/index.html", {
        "employees": employees,
        "positions": positions,
        "halls": halls,
        "users": users,
    })

def get_object_or_none(model, id):
    if id and str(id).isdigit():
        try:
            return model.objects.get(id=int(id))
        except model.DoesNotExist:
            return None
    return None

def create(request):
    if request.method == "POST":
        try:
            employee = Employee()
            employee.full_name = request.POST.get("full_name")
            employee.phone = request.POST.get("phone")
            employee.email = request.POST.get("email")
            employee.bio = request.POST.get("bio", "")
            employee.date_of_birth = request.POST.get("date_of_birth")

            user_id = request.POST.get("user")
            employee.user = get_object_or_none(AdmUser, user_id)

            position_id = request.POST.get("position")
            employee.position = get_object_or_none(Position, position_id)

            if 'photo' in request.FILES:
                employee.photo = request.FILES['photo']

            employee.work_description = request.POST.get("work_description", "")

            employee.full_clean()

            employee.save()

            halls_ids = request.POST.getlist("halls")
            halls_objs = Hall.objects.filter(id__in=halls_ids)
            employee.halls.set(halls_objs)

            messages.success(request, "Employee created successfully!")
            return HttpResponseRedirect("/employees/")

        except ValidationError as ve:
            messages.error(request, f"Validation error: {ve.message_dict}")
        except Exception as e:
            messages.error(request, f"Error creating employee: {str(e)}")

    positions = Position.objects.all()
    halls = Hall.objects.all()
    users = AdmUser.objects.all()
    return render(request, "crud_employee/create.html", {
        "positions": positions,
        "halls": halls,
        "users": users,
    })

def edit(request, id):
    try:
        employee = Employee.objects.get(id=id)

        if request.method == "POST":
            try:
                employee.full_name = request.POST.get("full_name")
                employee.phone = request.POST.get("phone")
                employee.email = request.POST.get("email")
                employee.bio = request.POST.get("bio", "")
                employee.date_of_birth = request.POST.get("date_of_birth")

                user_id = request.POST.get("user")
                employee.user = get_object_or_none(AdmUser, user_id)

                position_id = request.POST.get("position")
                employee.position = get_object_or_none(Position, position_id)

                if 'photo' in request.FILES:
                    employee.photo = request.FILES['photo']

                employee.work_description = request.POST.get("work_description", "")

                employee.full_clean()
                employee.save()

                halls_ids = request.POST.getlist("halls")
                halls_objs = Hall.objects.filter(id__in=halls_ids)
                employee.halls.set(halls_objs)

                messages.success(request, "Employee updated successfully!")
                return HttpResponseRedirect("/employees/")

            except ValidationError as ve:
                messages.error(request, f"Validation error: {ve.message_dict}")
            except Exception as e:
                messages.error(request, f"Error updating employee: {str(e)}")

        positions = Position.objects.all()
        halls = Hall.objects.all()
        users = AdmUser.objects.all()

        return render(request, "crud_employee/edit.html", {
            "employee": employee,
            "positions": positions,
            "halls": halls,
            "users": users,
        })

    except Employee.DoesNotExist:
        return HttpResponseNotFound(employee_not_found)

def delete(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
    except Employee.DoesNotExist:
        messages.error(request, "Employee not found")
    return HttpResponseRedirect("/employees/")

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сотрудник успешно создан')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'crud_employee/form.html', {'form': form, 'title': 'Добавить сотрудника'})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сотрудник успешно обновлен')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'crud_employee/form.html', {'form': form, 'title': 'Редактировать сотрудника'})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Сотрудник удалён')
        return redirect('employee_list')
    return render(request, 'crud_employee/confirm_delete.html', {'employee': employee})
