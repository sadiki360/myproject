from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Student  
from teacher.models import Teacher
from subject.models import Subject
from department.models import Department

@login_required
def index(request):
    count_students = Student.objects.count()
    count_teachers = Teacher.objects.count()
    count_subjects = Subject.objects.count()
    count_depts = Department.objects.count()

    context = {
        'count_students': count_students,
        'count_teachers': count_teachers,
        'count_subjects': count_subjects,
        'count_departments': count_depts,
    }
    return render(request, 'index.html', context)