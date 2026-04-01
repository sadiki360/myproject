from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10,
        choices=[('Male','Male'), ('Female','Female')])
    date_of_birth = models.DateField()
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField()
    subject_specialty = models.CharField(max_length=100)
    teacher_image = models.ImageField(upload_to='teachers/', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"