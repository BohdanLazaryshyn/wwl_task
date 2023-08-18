from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Order(models.Model):
    task_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.task_id} - {self.name}"
