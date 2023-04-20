from django.urls import path

from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('timetable', views.timetable, name='timetable'),
    path('materials', views.materials, name='materials'),
    path('contacts', views.contacts, name='contacts'),
    path('index', views.index, name='index'),
]
