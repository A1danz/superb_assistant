from django.shortcuts import render
from .models import Post, AttendanceLog, Contact, StudyMaterial, Student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signin(request):
    return render(request, "main/signin.html")


def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    return render(request, "main/signup.html")


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
