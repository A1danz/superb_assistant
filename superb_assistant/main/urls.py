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
    path('add_data', views.add_data, name='add_data'),
    path('edit_data', views.edit_data, name='edit_data'),
    path('delete_data', views.delete_data, name='delete_data'),
    path('materials/add_data', views.add_data, name='add_data'),
    path('materials/edit_data', views.edit_data, name='edit_data'),
    path('materials/delete_data', views.delete_data, name='delete_data'),
    path('contacts/add_data', views.add_data, name='add_data'),
    path('contacts/edit_data', views.edit_data, name='edit_data'),
    path('contacts/delete_data', views.delete_data, name='delete_data'),

]
