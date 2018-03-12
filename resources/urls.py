from django.urls import path

from . import views

urlpatterns = [
    path('resources/', views.resources, name='resources'),
    path('london/', views.london, name='london'),
    path('mississauga/', views.mississauga, name='mississauga'),
    path('waterloo/', views.waterloo, name='waterloo'),
    path('registration/', views.registration, name='registration'),
    path('thank_you/', views.thank_you, name='thank_you'),
]