from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpage, name='endpage'),
    path('create/', views.create, name='create'),
    path('unic/', views.unic, name='unic'),
]
