from dev.models import Profile
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
def dev_home(request):
    return render(request, 'dev/home.html')


# class dev_home(ListView):
#     model = Profile
