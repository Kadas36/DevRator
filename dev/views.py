from dev.models import Profile
from django.shortcuts import render
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def dev_home(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'dev/home.html', context)

