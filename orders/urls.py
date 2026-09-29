from django.urls import path
from .views import *

urlpatterns = [
    path('add_address/',add_address,name='add_address'),
    path('address_list/',address_list,name='address_list'),
    path('update_address/<int:pk>',update_address,name='update_address')
]