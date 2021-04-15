from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog_home(request):
    return render(request,'blog/blog_home.html')
    # return HttpResponse("<h1>blog Home</h2>")