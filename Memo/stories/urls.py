from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.endpage, name='endpage'),
    path('create', views.create, name='create')
]