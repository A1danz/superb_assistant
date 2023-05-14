import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import upper
from django.template.defaulttags import register

from .models import Post, AttendanceLog, Contact, StudyMaterial, Student, Lesson, Room
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, FileResponse
from .forms import Loginform, LessonForm


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
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
                return redirect('profile')
                # return render(request, 'main/profile.html')
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
    if request.user.is_authenticated:
        return redirect('index')
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
                student = Student.objects.create(room=room, user=new_user, state=2)
                student.save()
                return redirect('profile')
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


#
# @login_required()
# class ShowPost(ListView):
#     model = Post
#     template_name = 'main/index.html'
#     context_object_name = 'posts'
#     c = get_student(request)
#     def get_queryset(self):
#         return Post.objects.filter(room=cur_student.room)


@login_required()
def index(request):
    print(request.user)
    if request.method == "POST":
        print("board post-requets")
        print("board post-requets")
    cur_student = get_student(request)
    posts = Post.objects.filter(room=cur_student.room).order_by('-time')
    # if request.method == "POST":
    #     print(request.POST)
    #     for key in request.POST.keys():
    #         if "delete" in key:
    #             print(key)

    contex = {
        'posts': posts,
        'navbar': 'index',
        'perm': get_perm(cur_student.permission)
    }

    return render(request, "main/index.html", context=contex)


@login_required()
def contacts(request):
    cur_student = get_student(request)
    contacts = Contact.objects.filter(room=cur_student.room).order_by('-id')

    contex = {
        'contacts': contacts,
        'navbar': 'contacts',
        'perm': get_perm(cur_student.permission)
    }

    return render(request, "main/contact.html", context=contex)


@login_required()
def materials(request):
    if request.method == "POST":
        print("123")
    cur_student = get_student(request)
    materials = StudyMaterial.objects.filter(room=cur_student.room).order_by('-id')

    contex = {
        'materials': materials,
        'navbar': 'materials',
        'perm': get_perm(cur_student.permission)
    }

    return render(request, "main/train_material.html", context=contex)


@login_required()
def timetable(request):
    cur_student = get_student(request)
    if request.method == "POST":
        st = ""
        for i in request.POST.keys():
            if i.find('*'):
                st = i
        num = st[-1]
        day = st[0]
        lesson = Lesson.objects.get(schedule=cur_student.room, num=num, day=day)
        lesson.start_time = request.POST['start_time']
        lesson.end_time = request.POST['end_time']
        lesson.name = upper(request.POST['name']).strip()
        lesson.room_num = request.POST['room_num']
        lesson.schedule = cur_student.room
        lesson.save()
    list = Lesson.objects.filter(schedule=cur_student.room)
    if not list.exists():
        create_schedule(cur_student.room)
    dict_of_lessons = {}
    for i in range(1, 7):
        dict_of_lessons[i] = list.filter(day=i)
    DAY = {
        1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота'
    }

    contex = {
        'navbar': 'timetable',
        'DAY': DAY,
        'perm': get_perm(cur_student.permission),
        'data': dict_of_lessons
    }

    return render(request, "main/timetable.html", context=contex)


@login_required()
def log(request):
    cur_student = get_student(request)
    if request.method == "POST":
        request.session['lesson_name'] = list(request.POST.keys())[1]
        return redirect('lesson')
    lessons = set()
    data = Lesson.objects.filter(schedule=cur_student.room).values_list('name')
    for name in data:
        lesson = name[0]
        if lesson is not '':
            lessons.add(lesson)

    contex = {
        'perm': get_perm(cur_student.permission),
        'log': log,
        'navbar': 'log',
        'lessons': lessons
    }
    return render(request, "main/log.html", context=contex)


@login_required()
def lesson(request):
    cur_student = get_student(request)
    cur_lesson = request.session.get('lesson_name')
    group = Student.objects.filter(room=cur_student.room)
    data = AttendanceLog.objects.filter(room=cur_student.room, lesson=cur_lesson)
    dates_iterator = data.values_list('date').iterator()
    dates = set(i for i in dates_iterator)
    list_of_students_by_date = {}

    for i in dates:
        temp = data.filter(date=i[0])
        list_by_status = {}
        for j in temp:
            list_by_status[j.status] = j.students.all()
        list_of_students_by_date[i] = list_by_status

    contex = {
        'perm': get_perm(cur_student.permission),
        'group': group,
        'lesson_name': cur_lesson,
        'data_by_date': list_of_students_by_date
    }
    return render(request, "main/lesson.html", context=contex)


@login_required()
def lesson_edit(request):
    cur_student = get_student(request)
    group = Student.objects.filter(room=cur_student.room)
    contex = {
        'group': group,
        'lesson_name': request.session.get('lesson_name')
    }
    return render(request, "main/lesson_edit.html", context=contex)


@login_required()
def profile(request):
    cur_student = get_student(request)
    if request.method == 'POST':
        if request.POST.get('exit'):
            request.session.clear()
            logout(request)
            return redirect('signin')
        if request.POST.get('firstname'):
            request.user.first_name = request.POST['firstname']
        if request.POST.get('lastname'):
            request.user.last_name = request.POST['lastname']
        if request.POST.get('email'):
            request.user.email = request.POST['email']
        if request.POST.get('room'):
            room = cur_student.room
            room.name = request.POST['room']
            room.save()
        if request.user.check_password(request.POST.get('pass', False)):
            if request.POST['password1'] == request.POST['password2']:
                request.user.set_password(request.POST['password1'])
        request.user.save()
        for key in request.POST.keys():
            if 'del' in key:
                student = User.objects.get(username=key.split()[-1])
                student = Student.objects.get(user=student.id)
                student.permission = 0
                student.save()
            if 'add' in key:
                student = User.objects.get(username=key.split()[-1])
                student = Student.objects.get(user=student.id)
                student.permission = 1
                student.save()

    STATUS = {
        0: 'студент',
        1: 'заместитель старосты',
        2: 'староста'
    }
    group = Student.objects.filter(room=cur_student.room)
    room_name = cur_student.room.name
    contex = {
        'navbar': 'profile',
        'cur_student': cur_student,
        'perm': cur_student.permission,
        'status': STATUS.get(cur_student.permission),
        'group': group,
        'room_name': room_name,
        'STATUS': STATUS
    }
    return render(request, "main/profile.html", context=contex)

@register.filter
def get_item(dict, key):
    return dict.get(key)


@login_required()
def download_material(request, video_id):
    # TODO: сделать верификацию пользователя
    obj = StudyMaterial.objects.get(id=video_id)
    filename = obj.file.path

    return FileResponse(open(filename, 'rb'), as_attachment=True)


def get_student(request):
    return Student.objects.get(user=request.user)


def get_perm(permission):
    if permission == 0:
        return False
    return True


def create_schedule(room):
    default_time = (
        ('8:30', '10:00'),
        ('10:10', '11:40'),
        ('12:10', '13:40'),
        ('13:50', '15:20'),
        ('15:50', '17:20'),
        ('17:30', '19:00'),
        ('19:10', '20:40')
    )

    for i in range(1, 7):
        k = 1
        for time in default_time:
            Lesson.objects.create(day=i, start_time=time[0], end_time=time[1], schedule=room, num=k)
            k = k + 1

def add_post(request):
    print("hi")
    if request.method == "POST":
        print("Hi", request.user)
        print(request.POST)
        return HttpResponse("Ok")

