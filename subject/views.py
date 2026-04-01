from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Subject
from teacher.models import Teacher
from department.models import Department

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        description = request.POST.get('description')
        teacher_id = request.POST.get('teacher')
        department_id = request.POST.get('department')
        teacher = Teacher.objects.get(id=teacher_id) if teacher_id else None
        department = Department.objects.get(id=department_id) if department_id else None
        Subject.objects.create(
            name=name,
            code=code,
            description=description,
            teacher=teacher,
            department=department
        )
        messages.success(request, 'Subject added successfully!')
        return redirect('subject_list')
    teachers = Teacher.objects.all()
    departments = Department.objects.all()
    return render(request, 'subjects/add-subject.html', {'teachers': teachers, 'departments': departments})

def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')
        subject.description = request.POST.get('description')
        teacher_id = request.POST.get('teacher')
        department_id = request.POST.get('department')
        subject.teacher = Teacher.objects.get(id=teacher_id) if teacher_id else None
        subject.department = Department.objects.get(id=department_id) if department_id else None
        subject.save()
        messages.success(request, 'Subject updated successfully!')
        return redirect('subject_list')
    teachers = Teacher.objects.all()
    departments = Department.objects.all()
    return render(request, 'subjects/edit-subject.html', {'subject': subject, 'teachers': teachers, 'departments': departments})

def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    messages.success(request, 'Subject deleted successfully!')
    return redirect('subject_list')