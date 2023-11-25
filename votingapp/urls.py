from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_register', views.user_register, name='user_register'),
    path('user_registration', views.user_registration, name='user_registration'),
    path('user_login', views.user_login, name='user_login'),
    path('user_home', views.user_home, name='user_home'),



    
]