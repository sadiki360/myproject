from django.contrib import admin
from .models import Exam, ExamResult

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'exam_date', 'total_marks')
    search_fields = ('name', 'subject__name')
    list_filter = ('subject', 'exam_date')

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks_obtained', 'grade')
    search_fields = ('student__first_name', 'exam__name')
    list_filter = ('exam', 'grade')