from __future__ import absolute_import, unicode_literals

from celery import shared_task

from producer.models import Order, Employee
from random import randint


@shared_task
def add_new_order():
    print("Adding new order")
    employees = Employee.objects.all().count()
    if employees == 0:
        employee = Employee(
            username="first_employee",
            first_name="First",
            last_name="Employee",
            email="first@employee.com",
            password="12345678",
            position="First position",
            probation=False,
        )
        employee.save()
    employee = Employee.objects.all()[randint(0, employees - 1)]
    task_id = randint(1, 1000)
    order = Order(
        task_id=task_id,
        name=f"Order {randint(1, 1000)}",
        description=f"Description for order {task_id}",
        employee=employee,
    )
    order.save()
    return order.id
