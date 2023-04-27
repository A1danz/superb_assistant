from django.urls import path

from . import views
# from .views import RegisterUser

urlpatterns = [
    # path('signin', RegisterUser.as_view(), name='signin'),
    path('signin', views.signin, name='signin'),
    path('signup/', views.signup, name='signup/'),
    path('profile', views.profile, name='profile'),
    path('timetable', views.timetable, name='timetable'),
    path('materials', views.materials, name='materials'),
    path('contacts', views.contacts, name='contacts'),
    path('index', views.index, name='index'),
    path('log', views.log, name='log'),
    path('lesson', views.lesson, name='lesson'),
    path('lesson_edit', views.lesson_edit, name='lesson_edit')
]
