from django.db import models
from student.models import Student
from subject.models import Subject

class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name='exams'
    )
    exam_date = models.DateField()
    total_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class ExamResult(models.Model):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE,
        related_name='results'
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='results'
    )
    marks_obtained = models.IntegerField(default=0)
    grade = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks_obtained}"