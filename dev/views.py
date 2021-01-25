from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required
from .forms import projectForm, profileForm, reviewForm
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse

from rest_framework import status
from .permissions import IsAdminOrReadOnly



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
            if request.method == 'POST':
                form = projectForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.developer = profile
                    post.save()
                    return redirect('home')
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
    
    reviews = Review.objects.filter(project=project_id)

    design_rating_average = reviews.aggregate(Avg("design_rating"))["design_rating__avg"]
    if design_rating_average == None:
        design_average = 0
    else:
        design_average = round(design_rating_average,1)

    usability_rating_average = reviews.aggregate(Avg("usability_rating"))["usability_rating__avg"]
    if usability_rating_average == None:
        usability_average = 0
    else:
        usability_average = round(usability_rating_average,1)

    content_rating_average = reviews.aggregate(Avg("content_rating"))["content_rating__avg"]
    if content_rating_average == None:
        content_average = 0
    else:    
        content_average = round(content_rating_average,1)

    sum = design_average+usability_average+content_average
    average = round(int(sum)/3,2)
    
    current_user_profile=[]
    for profile in all_profiles:
        if current_user_id:
            current_user_profile = profile
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

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)   

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    permission_classes = (IsAdminOrReadOnly,)  

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)    

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        



class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)   

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

    permission_classes = (IsAdminOrReadOnly,)   

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)   

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                          