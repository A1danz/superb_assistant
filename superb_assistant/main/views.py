from django.contrib.auth.decorators import login_required
from django.forms.utils import ErrorDict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout

from .models import Post, AttendanceLog, Contact, StudyMaterial, Student, Lesson, Room
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from .forms import Loginform


def signin(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        user_value = ''
        password_value = ''
        form = Loginform(request.POST or None)
        if form.is_valid():
            user_value = form.cleaned_data.get("username")
            password_value = form.cleaned_data.get("password")

            user = authenticate(username=user_value, password=password_value)
            if user is not None:
                login(request, user)
                return render(request, 'main/profile.html')
            else:
                context = {'form': form,
                           'error': 'Логин или пароль неверны'}
                return render(request, 'main/signin.html', context)

        else:
            json_data = form.errors.get_json_data()
            print(json_data)
            context = {'form': form, 'username_error': '', 'password_error': ''}
            if 'username' in json_data:
                context['username_error'] = json_data['username'][0]['message']
            if 'password' in json_data:
                context['password_error'] = json_data['password'][0]['message']
            return render(request, 'main/signin.html', context)
    else:
        return render(request, 'main/signin.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        print(user_form.errors)
        print(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.first_name = request.POST['name']
            new_user.last_name = request.POST['surname']
            new_user.save()
            if request.POST['role'] == 'warden':
                return HttpResponse("You have to wait")
            else:
                room = Room.objects.get(pk=request.POST['roomnum'])
                # student = Student.objects.create(room=Room.objects.get(pk=request.POST['roomnum']), user=new_user)
                student = Student.objects.create(room=room, user=new_user)
                student.save()
                return redirect(profile)
        else:
            return HttpResponse("no")
            # render(request, "main/signup.html") #??
            # надо наверно добавить как-то, чтобы показывалось почему введенные данные некорректные
    else:
        return render(request, "main/signup.html")


@login_required()
def index(request):
    if request.user.is_authenticated:
        print(request.user.last_name)
    posts = Post.objects.all()

    contex = {
        'posts': posts,
        'navbar': 'index'
    }

    return render(request, "main/index.html", context=contex)


@login_required()
def contacts(request):
    contacts = Contact.objects.all()

    contex = {
        'contacts': contacts,
        'navbar': 'contacts'
    }

    return render(request, "main/contact.html", context=contex)


@login_required()
def materials(request):
    materials = StudyMaterial.objects.all()

    contex = {
        'materials': materials,
        'navbar': 'materials'
    }

    return render(request, "main/train_material.html", context=contex)


@login_required()
def timetable(request):
    list = Lesson.objects.all()

    contex = {
        'list': list,
        'navbar': 'timatable'
    }

    return render(request, "main/timetable.html", context=contex)


@login_required()
def log(request):
    lessons = AttendanceLog.objects.all()

    contex = {
        'lessons': lessons,
        'navbar': 'log'
    }
    return render(request, "main/log.html", context=contex)


@login_required()
def lesson(request):
    contex = {}
    return render(request, "main/lesson.html", context=contex)


@login_required()
def lesson_edit(request):
    contex = {}
    return render(request, "main/lesson_edit.html", context=contex)


@login_required()
def profile(request):
    if request.method == 'POST':
        print(request.POST)
        request.user.firstname = request.POST['name']
        request.user.lastname = request.POST['surname']
        student = Student.objects.create(user=request.user)
        student.save()
        return HttpResponse("created user")
    else:
        students = Student.objects.all()
        room = ''
        user = ''
        contex = {
            'students': students,
            'navbar': 'profile'
        }
        return render(request, "main/profile.html", context=contex)
