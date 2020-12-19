from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpage, name='endpage'),
    path('create/', views.create, name='create'),
    # path('<int:pk>', views.StoriesDetailView.as_view(), name='stories-detail')
]