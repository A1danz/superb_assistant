from django.shortcuts import render
from .models import Post, AttendanceLog, Contact, StudyMaterial, Student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signin(request):
    return render(request, "main/signin.html")


def signup(request):
    # if request.method == 'POST':
    #     user_form = UserRegistrationForm(request.POST)
    #     if user_form.is_valid():
    #         # Create a new user object but avoid saving it yet
    #         new_user = user_form.save(commit=False)
    #         # Set the chosen password
    #         new_user.set_password(user_form.cleaned_data['password'])
    #         # Save the User object
    #         new_user.save()
    #         return render(request, 'account/register_done.html', {'new_user': new_user})
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
