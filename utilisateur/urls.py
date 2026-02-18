
from django.urls import path
from . import views

app_name = 'utilisateur'

urlpatterns = [
    #acceuil
    path('', views.splash, name='splash'),
    path('home/kovoit/', views.home, name='home'),


    #inscription
    path("inscritption/", views.inscription, name='inscription'),
    path("commpte/creer/", views.compte_create, name='compte_creer'),

    #connection
    path('bienvenue/', views.welcome, name='welcome'),
    path('connection/phone/', views.connection_phone, name='connection_phone'),
    path('verification/phone/', views.verification_phone, name='verification_phone'),
    path('connection/reussi/', views.connection_reussi, name='connection_reussi')
]