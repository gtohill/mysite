from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('parents/', views.parents, name='parents'),
    path('courses/', views.courses, name='courses'),
    path('beginner/', views.beginner, name='beginner'),
    path('novice/', views.novice, name='novice'),
    path('intermediate/', views.intermediate, name='intermediate'),
    path('rasppi/', views.rasppi, name='rasppi'),
    path('webdesign/', views.webdesign, name='webdesign'),
]
