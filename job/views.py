from django.shortcuts import render,HttpResponse


# Create your views here.
def addjob(request):
    return render(request, 'addjob.html')
