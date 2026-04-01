from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Exam, ExamResult
from subject.models import Subject
from student.models import Student

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams/exams.html', {'exams': exams})

def add_exam(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject_id = request.POST.get('subject')
        exam_date = request.POST.get('exam_date')
        total_marks = request.POST.get('total_marks')
        subject = Subject.objects.get(id=subject_id) if subject_id else None
        Exam.objects.create(
            name=name,
            subject=subject,
            exam_date=exam_date,
            total_marks=total_marks
        )
        messages.success(request, 'Exam added successfully!')
        return redirect('exam_list')
    subjects = Subject.objects.all()
    return render(request, 'exams/add-exam.html', {'subjects': subjects})

def edit_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        exam.name = request.POST.get('name')
        subject_id = request.POST.get('subject')
        exam.subject = Subject.objects.get(id=subject_id) if subject_id else None
        exam.exam_date = request.POST.get('exam_date')
        exam.total_marks = request.POST.get('total_marks')
        exam.save()
        messages.success(request, 'Exam updated successfully!')
        return redirect('exam_list')
    subjects = Subject.objects.all()
    return render(request, 'exams/edit-exam.html', {'exam': exam, 'subjects': subjects})

def delete_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    messages.success(request, 'Exam deleted successfully!')
    return redirect('exam_list')

def result_list(request):
    results = ExamResult.objects.all()
    return render(request, 'exams/results.html', {'results': results})

def add_result(request):
    if request.method == 'POST':
        exam_id = request.POST.get('exam')
        student_id = request.POST.get('student')
        marks_obtained = request.POST.get('marks_obtained')
        grade = request.POST.get('grade')
        exam = Exam.objects.get(id=exam_id) if exam_id else None
        student = Student.objects.get(id=student_id) if student_id else None
        ExamResult.objects.create(
            exam=exam,
            student=student,
            marks_obtained=marks_obtained,
            grade=grade
        )
        messages.success(request, 'Result added successfully!')
        return redirect('result_list')
    exams = Exam.objects.all()
    students = Student.objects.all()
    return render(request, 'exams/add-result.html', {'exams': exams, 'students': students})