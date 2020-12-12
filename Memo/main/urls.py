from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('Slider', views.slider)
]
