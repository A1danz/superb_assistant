from django import forms

from .models import Lesson


class Loginform(forms.Form):
    username = forms.CharField(max_length=25, label="Enter username")
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['start_time', 'end_time', 'name', 'room_num']

