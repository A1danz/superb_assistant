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
    uservalue = ''
    passwordvalue = ''

    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            return render(request, 'main/profile.html')
        else:
            context = {'form': form,
                       'error': 'Логин и пароль неверны'}
            return render(request, 'main/signin.html', context)

    else:
        print("Form is invalid")
        json_data = form.get_json_data()
        context = {'form': form}
        context['username_error'] = ''
        context['password_error'] = ''
        if (json_data['username']):
            context['username_error'] = json_data['username'][0]['message']
        if (json_data['password']):
            context['password_error'] = json_data['password'][0]['message']
        return render(request, 'main/signin.html', context)


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        print(user_form.errors)
        print(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.first_name=request.POST['name']
            new_user.last_name=request.POST['surname']
            new_user.save()
            if request.POST['role'] == 'warden':
                return HttpResponse("You have to wait")
            else:
                room = Room.objects.get(pk=request.POST['roomnum'])
                #student = Student.objects.create(room=Room.objects.get(pk=request.POST['roomnum']), user=new_user)
                student = Student.objects.create(room=room, user=new_user)
                student.save()
                return redirect(profile)
        else:
            return HttpResponse("no")
                #render(request, "main/signup.html") #??
            #надо наверно добавить как-то, чтобы показывалось почему введенные данные некорректные
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
    list = Lesson.objects.all()

    contex = {
        'list': list,
        'navbar': 'timatable'
    }

    return render(request, "main/timetable.html", context=contex)


def log(request):
    lessons = AttendanceLog.objects.all()

    contex = {
        'lessons': lessons,
        'navbar': 'log'
    }
    return render(request, "main/log.html", context=contex)


def lesson(request):
    contex = {}
    return render(request, "main/lesson.html", context=contex)


def lesson_edit(request):
    contex = {}
    return render(request, "main/lesson_edit.html", context=contex)


@login_required
def profile(request):
    if request.method == 'POST':
        request.user.firstname = request.POST['name']
        request.user.lastname = request.POST['surname']
        student = Student.objects.create(user=request.user)
        student.save()
        return HttpResponse("created user")
    else:
        students = Student.objects.all()
        contex = {
            'students': students,
            'navbar': 'profile'
        }
        return render(request, "main/profile.html", context=contex)


# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = "main/signup.html"
#     success_url = reverse_lazy('signin')