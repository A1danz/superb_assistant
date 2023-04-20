from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('timetable', views.timetable, name='timetable'),
    path('materials', views.materials, name='materials'),
    path('contacts', views.contacts, name='contacts'),
    path('index', views.index, name='index'),
]
