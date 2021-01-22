from django.shortcuts import render

# Create your views here.
def dev_home(request):
    return render(request, 'dev/home.html')
