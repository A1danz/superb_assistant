from django.contrib import admin

from .models import Room, Student, Schedule, AttendanceLog, Post, StudyMaterial, Contact, Lesson

admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Lesson)
admin.site.register(AttendanceLog)
admin.site.register(Post)
admin.site.register(StudyMaterial)
admin.site.register(Contact)

# Register your models here.
