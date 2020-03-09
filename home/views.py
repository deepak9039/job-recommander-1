from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = User.objects.create_user(username=username,password=password,email=email,first_name=name)
        user.save()
        auth.login(request,user)
        param = {
            "user" : user
        }
        return render(request,"profile.html",param)
    return render(request,'signup.html')

def login(request):
    return render(request,'profile.html')