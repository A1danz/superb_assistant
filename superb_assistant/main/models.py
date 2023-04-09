import datetime
import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models

def rand():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
#генерируем случайную строку

class Room(models.Model):
    code = models.CharField(max_length=10, unique=True, default = rand)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    SIMPLE_STUDENT = 0
    STUDENT_WITH_CAPABILITIES = 1
    HEADMAN = 2

    PERMISSION = [
        (SIMPLE_STUDENT, 'Обычный студент'),
        (STUDENT_WITH_CAPABILITIES, 'Студент с дополнительными возможностями'),
        (HEADMAN, 'Староста')

    ]
    permission = models.SmallIntegerField(choices=PERMISSION, default=SIMPLE_STUDENT)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField
    last_name = models.CharField

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField
    time = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    lesson_time = models.TimeField
    lesson_on_monday = models.CharField(max_length=50, blank=True)
    lesson_on_tuesday = models.CharField(max_length=50, blank=True)
    lesson_on_wednesday = models.CharField(max_length=50, blank=True)
    lesson_on_thursday = models.CharField(max_length=50, blank=True)
    lesson_on_friday = models.CharField(max_length=50, blank=True)
    lesson_on_saturday = models.CharField(max_length=50, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class AttendanceLog(models.Model):
    ILL = "ill"
    ABSENT = "abs"
    BE = "be"
    VALID_REASON = "vr"

    STATUS = [
        (ILL, 'Болеет'),
        (ABSENT, 'Отсутствует'),
        (VALID_REASON, 'Уважительная причина'),
        (BE, 'Присутствует')
    ]

    students = models.ManyToManyField(Student)
    status = models.CharField(max_length=3, choices=STATUS, default=BE)
    date = models.DateField(default=datetime.date.today())
    lesson = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class StudyMaterial(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    lesson = models.CharField(max_length=50, blank=True)
    teacher = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher
