from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('slider', views.slider)
]
