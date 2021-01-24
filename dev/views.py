from django.db.models.expressions import Random
import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required
from .forms import projectForm, profileForm, reviewForm
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
    current_user_id = current_user.id
    current_user_profile = Profile.objects.filter(user=current_user)
    all_profiles = Profile.objects.all()

    for profile in all_profiles:
        if current_user_id:
            if request.method == 'POST':
                form = projectForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.developer = profile
                    post.save()
                    return redirect('newpost')
            else:
                form = projectForm()

    context = {
        "form": form,
    }

    return render(request, 'dev/new_project.html', context)  


@login_required(login_url='/accounts/login/')
def profileView(request):
    current_user = request.user 
    all_profiles = Profile.objects.all()
    current_user_id = current_user.id    
    curentProfile = Profile.objects.get(id=current_user_id)

    print(curentProfile)

    form = profileForm( instance= curentProfile)
    
    for profile in all_profiles:
        if current_user_id:
            if request.method == 'POST':
                form = profileForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            
    cp=[]
    cpp = []
    for profile in all_profiles:
        if current_user_id:
            cp = profile
            cpp = Project.objects.filter(developer=cp)
            
            
    context = {
        "cp": cp,
        'cpp': cpp,
        'form': form
    }

    return render(request, 'dev/profile.html', context)


@login_required(login_url='/accounts/login/')
def Reviewview(request, project_id):
    form = reviewForm()
    project = get_object_or_404(Project, id=project_id)
    current_user = request.user
    project_reviews = Review.objects.filter(project=project_id)
    all_profiles = Profile.objects.all()
    current_user_id = current_user.id

    for profile in all_profiles:
        if current_user_id:
            if request.method == 'POST':
                form = reviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.project = project
                    review.reviewer = profile
                    review.save()
                    return redirect('home')
            else:
                form = reviewForm()

    context = {
        "project": project,
        "form": form,
        'project_reviews': project_reviews
    }
    return render(request, 'dev/review.html', context)       