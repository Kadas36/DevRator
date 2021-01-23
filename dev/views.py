from django.db.models.expressions import Random
import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required
from .forms import projectForm
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


@login_required(login_url='/accounts/login/')
def new_project(request):
    form = projectForm()
    current_user = request.user
    
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.developer.user = current_user
            post.save()
            return redirect('newpost')
    else:
        form = projectForm()

    context = {
        "form": form,
    }

    return render(request, 'dev/new_project.html', context)  

