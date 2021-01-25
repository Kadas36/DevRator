from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.dev_home, name='home'),
    path('project/', views.new_project, name='newpost'),
    path('profile/', views.profileView, name='profile'),
    path('project/<int:project_id>/', views.Reviewview, name='review'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profile/profile-id/<int:pk>/',views.ProfileDescription.as_view()),
    path('api/project/project-id/<int:pk>/',views.ProjectDescription.as_view()),
]

