from django.shortcuts import render
from .models import Post, AttendanceLog

from django.http import HttpResponse


def index(request):
    posts = Post.objects.all()
    return render(request, "main/index.html", {'posts': posts})


def contacts(request):
    return render(request, "main/contacts.html")


def post(request):
    return HttpResponse("this page about posts")


def materials(request):
    return HttpResponse("this page about study materials")


def attend(request):
    list = AttendanceLog.objects.all()
    return render(request, "main/attendance log.html", {'list': list})
