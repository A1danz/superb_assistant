from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models


class Student(User):
    user_permissions = models.SmallIntegerField


class Group(Group):
    code = models.CharField


class Post(models.Model):
    title = models.CharField
    text = models.TextField
    time = models.TimeField


class Schedule(models.Model):
    lessons_time = models.TimeField
    lessons_on_monday = models.CharField
    lessons_on_tuesday = models.CharField
    lessons_on_wednesday = models.CharField
    lessons_on_thursday = models.CharField
    lessons_on_friday = models.CharField
    lessons_on_saturday = models.CharField


class AttendanceLog(models.Model):
    status = models.CharField(max_length=3)
    date = models.DateField
    lesson = models.TextField




