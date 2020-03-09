from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse,redirect
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
        return redirect("profile",username)
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["loginusername"]
        password = request.POST["loginpassword"]
        user = auth.authenticate(username=username,password=password)
        auth.login(request,user)

        return redirect("profile",username)
    return render(request,'profile.html')

def profile(request,username):
    user = User.objects.get(username=username)
    param = {
        "user" : user
    }
    return render(request,"profile.html",param)
