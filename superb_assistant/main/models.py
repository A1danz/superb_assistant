import datetime

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models


class Student(User):
    SIMPLE_STUDENT = 0
    STUDENT_WITH_CAPABILITIES = 1
    HEADMAN = 2

    PERMISSION = [
        (SIMPLE_STUDENT, 'Обычный студент'),
        (STUDENT_WITH_CAPABILITIES, 'Студент с дополнительными возможностями'),
        (HEADMAN, 'Староста')

    ]
    permission = models.SmallIntegerField(choices=PERMISSION, default=SIMPLE_STUDENT)
    room = models.OneToOneField(Group, on_delete=models.CASCADE())

    class Meta:
        proxy = True
        verbose_name = "Студент"

    def __str__(self):
        return f'{self.last_name} {self.fist_name}'


class Room(Group):
    code = models.CharField(unique=True)

    class Meta:
        proxy = True

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField
    time = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE())

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
    room = models.ForeignKey(Room, on_delete=models.CASCADE())


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
    room = models.ForeignKey(Room, on_delete=models.CASCADE())


class StudyMaterial(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField
    room = models.ForeignKey(Room, on_delete=models.CASCADE())

    def __str__(self):
        return self.name


class Contact(models.Model):
    lesson = models.CharField(max_length=50, blank=True)
    teacher = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE())

    def __str__(self):
        return self.teacher
