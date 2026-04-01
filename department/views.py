from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Department
from teacher.models import Teacher

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

@login_required
def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        head_teacher_id = request.POST.get('head_teacher')
        head_teacher = Teacher.objects.get(id=head_teacher_id) if head_teacher_id else None
        Department.objects.create(
            name=name,
            description=description,
            head_teacher=head_teacher
        )
        messages.success(request, 'Department added successfully!')
        return redirect('department_list')
    teachers = Teacher.objects.all()
    return render(request, 'departments/add-department.html', {'teachers': teachers})

@login_required
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        head_teacher_id = request.POST.get('head_teacher')
        department.head_teacher = Teacher.objects.get(id=head_teacher_id) if head_teacher_id else None
        department.save()
        messages.success(request, 'Department updated successfully!')
        return redirect('department_list')
    teachers = Teacher.objects.all()
    return render(request, 'departments/edit-department.html', {'department': department, 'teachers': teachers})

@login_required
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    messages.success(request, 'Department deleted successfully!')
    return redirect('department_list')