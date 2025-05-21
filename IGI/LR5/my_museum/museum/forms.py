from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'phone', 'email', 'bio', 'date_of_birth', 'halls', 'photo', 'work_description']
