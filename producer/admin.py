from django.contrib import admin

from producer.models import Order, Employee


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "task_id", "employee"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["username", "position", "probation"]
