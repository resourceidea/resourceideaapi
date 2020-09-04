from django.contrib import admin  # type: ignore

from employee.models import Employee

admin.site.register(Employee)
