from django.urls import path
from .views import *

urlpatterns=[
    path('',login_,name='login_'),
    path('register/',register,name='register'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('respasw/',respasw,name='respasw'),
    path('update_pro/',update_pro,name='update_pro'),
    path('forget_pasw/',forget_pasw,name='forget_pasw')
]