from django.db.models.expressions import Random
import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required
from .forms import projectForm, profileForm, reviewForm
from django.db.models import Avg
# Create your views here.

@login_required(login_url='/accounts/login/')
def dev_home(request):
    projects = Project.objects.all()
    lead_projects = Project.objects.order_by("?")
    lead_project = lead_projects.first()
    current_user = request.user
    current_user_id = current_user.id
    all_profiles = Profile.objects.all()
    current_user_profile=[]
    for profile in all_profiles:
        if current_user_id:
            current_user_profile = profile

    context = {
        'projects': projects,
        'lead_project': lead_project,
        'current_user_profile': current_user_profile,
    }

    return render(request, 'dev/home.html', context)

@login_required(login_url='/accounts/login/')
def new_project(request):
    form = projectForm()
    current_user = request.user
    current_user_id = current_user.id
    all_profiles = Profile.objects.all()

    current_user_profile=[]
    for profile in all_profiles:
        if current_user_id:
            current_user_profile = profile

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
        "current_user_profile": current_user_profile
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
            
    current_user_profile=[]
    cpp = []
    for profile in all_profiles:
        if current_user_id:
            current_user_profile = profile
            cpp = Project.objects.filter(developer=current_user_profile)
            
            
    context = {
        "ccurrent_user_profilep": current_user_profile,
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
    current_user_profile = Profile.objects.filter(user=current_user)

    reviews = Review.objects.filter(project=project_id)
    design_rating_average = reviews.aggregate(Avg("design_rating"))["design_rating__avg"]
    design_average = round(design_rating_average,1)
    usability_rating_average = reviews.aggregate(Avg("usability_rating"))["usability_rating__avg"]
    usability_average = round(usability_rating_average,1)
    content_rating_average = reviews.aggregate(Avg("content_rating"))["content_rating__avg"]
    content_average = round(content_rating_average,1)

    sum = design_average+usability_average+content_average
    average = round(int(sum)/3,2)
    
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
        "current_user_profile": current_user_profile,
        'project_reviews': project_reviews,
        "design_average": design_average,
        "usability_average": usability_average,
        "content_average": content_average,
        "average": average,
    }
    return render(request, 'dev/review.html', context)       