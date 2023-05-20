from django import forms

from .models import *


class Loginform(forms.Form):
    username = forms.CharField(max_length=25, label="Enter username")
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['start_time', 'end_time', 'name', 'room_num']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = '__all__'