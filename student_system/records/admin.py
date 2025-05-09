
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'course', 'education', 'admission_date')
    list_filter = ('course', 'education')  # 🎯 Adds filtering options

admin.site.register(Student, StudentAdmin)
