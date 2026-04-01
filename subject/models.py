from django.db import models
from teacher.models import Teacher
from department.models import Department

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='subjects'
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='subjects'
    )

    def __str__(self):
        return f"{self.name} ({self.code})"