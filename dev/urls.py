from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_home, name='home'),
    path('project/', views.new_project, name='newpost'),
]