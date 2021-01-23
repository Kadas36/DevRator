from django.db.models.expressions import Random
import random
from django.shortcuts import render
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def dev_home(request):
    projects = Project.objects.all()
    lead_projects = Project.objects.order_by("?")
    lead_project = lead_projects.first()
    print(lead_project)

    context = {
        'projects': projects,
        'lead_project': lead_project
    }

    return render(request, 'dev/home.html', context)

