from django.urls import path  # Change your import to this
from django.contrib import admin
from . import views

app_name = 'computers'

urlpatterns = [
    path('', views.IndexView, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'), # No regex needed!
    # path('computers/add/', views.ComputerCreate.as_view(), name='computer-add'),
]