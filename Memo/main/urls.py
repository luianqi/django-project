from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.layout),
    path('slider', views.slider)
]
