from django.shortcuts import render
from .models import Post, AttendanceLog, Contact, StudyMaterial, Student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

def signin(request):
    return render(request, "main/signin.html")


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        #это я выводила чтобы понять, считывается ли вообще что-то
        #спойлер - почему-то не считывается
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("Created")
        else:
            return profile(request)
    else:
        return render(request, "main/signup.html")


def index(request):
    posts = Post.objects.all()

    contex = {
        'posts': posts,
        'navbar': 'index'
    }

    return render(request, "main/index.html", context=contex)


def contacts(request):
    contacts = Contact.objects.all()

    contex = {
        'contacts': contacts,
        'navbar': 'contacts'
    }

    return render(request, "main/contact.html", context=contex)


def materials(request):
    materials = StudyMaterial.objects.all()

    contex = {
        'materials': materials,
        'navbar': 'materials'
    }

    return render(request, "main/train_material.html", context=contex)


def timetable(request):
    list = AttendanceLog.objects.all()

    contex = {
        'list': list,
        'navbar': 'timatable'
    }

    return render(request, "main/timetable.html", context=contex)


def profile(request):
    students = Student.objects.all()

    contex = {
        'students': students,
        'navbar': 'profile'
    }

    return render(request, "main/profile.html", context=contex)
