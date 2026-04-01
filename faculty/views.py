from django.shortcuts import render
from student.models import Student  # Importi l-models
from teacher.models import Teacher
from subject.models import Subject
from department.models import Department

def index(request):
    # Hna kankheliw Django i-7seb l-3adad
    count_students = Student.objects.count()
    count_teachers = Teacher.objects.count()
    count_subjects = Subject.objects.count()
    count_depts = Department.objects.count()

    context = {
        'count_students': count_students,
        'count_teachers': count_teachers,
        'count_subjects': count_subjects,
        'count_depts': count_depts,
    }
    return render(request, 'index.html', context)