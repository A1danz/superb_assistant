from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendance log', views.attend, name='attend'),
    path('study materials', views.materials, name='materials'),
    path('contacts', views.contacts, name='contacts'),
    path('notice board', views.post, name='post'),
]
