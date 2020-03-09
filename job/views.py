from django.shortcuts import render

# Create your views here.
def addjob(request):
    return render(request,'addjob.html')
