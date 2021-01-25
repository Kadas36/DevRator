from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_home, name='home'),
    path('project/', views.new_project, name='newpost'),
    path('profile/', views.profileView, name='profile'),
    path('project/<int:project_id>/', views.Reviewview, name='review'),
    path('api/users/', views.UserList.as_view())
]