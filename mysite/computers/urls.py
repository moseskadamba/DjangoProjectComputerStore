
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'computers'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9])/$', views.DetailView.as_view(), name='detail'),
    url(r'computers/add/$', views.ComputerCreate.as_view(), name='computer-add')
]
