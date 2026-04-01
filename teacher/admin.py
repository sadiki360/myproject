from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'teacher_id',
                    'gender', 'email', 'mobile_number', 'subject_specialty')
    search_fields = ('first_name', 'last_name', 'teacher_id', 'email')
    list_filter = ('gender', 'subject_specialty')