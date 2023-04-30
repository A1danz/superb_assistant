from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register

from .models import Post, AttendanceLog, Contact, StudyMaterial, Student, Lesson, Room
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import Loginform


def signin(request):
    if (request.user.is_authenticated):
        return redirect(index)
    if request.method == 'POST':
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
                           'error': 'Логин или пароль неверны'}
                return render(request, 'main/signin.html', context)

        else:
            json_data = form.errors.get_json_data()
            print(json_data)
            context = {'form': form}
            context['username_error'] = ''
            context['password_error'] = ''
            if ('username' in json_data):
                context['username_error'] = json_data['username'][0]['message']
            if ('password' in json_data):
                context['password_error'] = json_data['password'][0]['message']
            return render(request, 'main/signin.html', context)
    else:
        return render(request, 'main/signin.html')


def signup(request):
    if (request.user.is_authenticated):
        return redirect(index)
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.first_name = request.POST['name']
            new_user.last_name = request.POST['surname']
            if request.POST['role'] == 'warden':
                new_user.save()
                return HttpResponse("You have to wait")
            else:
                room = Room.objects.get(pk=request.POST['roomnum'])
                new_user.save()
                student = Student.objects.create(room=room, user=new_user)
                student.save()
                return redirect(profile)
        else:
            json_data = user_form.errors.get_json_data()
            list = request.POST
            context = {'form': user_form}
            if list['username'] == '' or list['password1'] == '' or list['password2'] == '':
                context['errors'] = "Заполните все поля"
            elif 'username' in json_data:
                context['errors'] = 'Пользователь с таким именем уже существует'
            elif 'password1' in json_data or 'password2' in json_data:
                context[
                    'errors'] = 'Введите корректные, совпадающие пароли! (сложный пароль, не похожий на логин, состоящий из букв, цифр и специальных символов, длиной не менее 8)'
            return render(request, "main/signup.html", context)
    else:
        return render(request, 'main/signup.html')


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

    DAY = {
        1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота'
    }

    contex = {
        'list': list,
        'navbar': 'timatable',
        'DAY': DAY
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
        if request.POST.get('exit'):
            request.session.clear()
            logout(request)
            return redirect(signup)
        print(request.POST)
        request.user.firstname = request.POST['name']
        request.user.lastname = request.POST['surname']
        student = Student.objects.create(user=request.user)
        student.save()
        return HttpResponse("created user")
    else:
        cur_student = Student.objects.get(user=request.user)

        STATUS = {
            0: 'студент',
            1: 'заместитель старосты',
            2: 'староста'
        }


        group = Student.objects.filter(room=cur_student.room)

        contex = {
            'navbar': 'profile',
            'cur_student': cur_student,
            'perm': cur_student.permission,
            'group': group,
            'STATUS': STATUS
        }
        return render(request, "main/profile.html", context=contex)


@register.filter
def get_item(dict, key):
    return dict.get(key)