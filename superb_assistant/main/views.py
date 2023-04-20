from django.shortcuts import render
from .models import Post, AttendanceLog, Contact, StudyMaterial, Student


def index(request):
    posts = Post.objects.all()
    return render(request, "main/index.html", {'posts': posts})


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "main/contact.html", {'contacts': contacts})


def materials(request):
    materials = StudyMaterial.objects.all()
    return render(request, "main/train_material.html")


def timetable(request):
    list = AttendanceLog.objects.all()
    return render(request, "main/timetable.html", {'list': list})


def profile(request):
    students = Student.objects.all()
    return render(request, "main/profile.html")
