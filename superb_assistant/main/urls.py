from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('timetable', views.timetable, name='timetable'),
    path('materials', views.materials, name='materials'),
    path('contacts', views.contacts, name='contacts'),
    path('log', views.log, name='log'),
    path('lesson', views.lesson, name='lesson'),
    path('lesson_edit', views.lesson_edit, name='lesson_edit'),
    path('materials/<int:video_id>', views.download_material, name='download_material'),
    path('add_post', views.add_post, name='add_post'),
    path('edit_post', views.edit_post, name='edit_post')
]
