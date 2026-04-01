from django.db import models
from teacher.models import Teacher

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    head_teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='headed_departments'
    )

    def __str__(self):
        return self.name