from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models


class Student(User):
    user_permissions = models.SmallIntegerField('Права', default=0)

    def __str__(self):
        return self.first_name


class Group(Group):
    code = models.CharField

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField
    time = models.TimeField


class Schedule(models.Model):
    lesson_time = models.TimeField
    lesson_on_monday = models.CharField
    lesson_on_tuesday = models.CharField
    lesson_on_wednesday = models.CharField
    lesson_on_thursday = models.CharField
    lesson_on_friday = models.CharField
    lesson_on_saturday = models.CharField


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

    status = models.CharField(max_length=3, choices=STATUS, default=BE)
    date = models.DateField
    lesson = models.TextField
