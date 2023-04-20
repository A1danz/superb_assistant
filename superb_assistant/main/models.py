import datetime
import random
import string

from django.contrib.auth.models import User
from django.db import models

# генерируем случайную строку
def rand():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))


class Room(models.Model):
    code = models.CharField(max_length=10, unique=True, default=rand)
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

    def __str__(self):
        return self.user.__str__()


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    DAY = [
        (MONDAY, 'Понедельник'),
        (THURSDAY, 'Вторник'),
        (WEDNESDAY, 'Среда'),
        (THURSDAY, 'Четверг'),
        (FRIDAY, 'Пятница'),
        (SATURDAY, 'Суббота')
    ]
    day = models.SmallIntegerField(choices=DAY)
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=50, blank=True)
    schedule = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day}: {self.name}'


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

    def __str__(self):
        return f'{self.date}: {self.lesson}'


class StudyMaterial(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()
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
