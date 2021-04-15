from django.shortcuts import render
from django.http import HttpResponse
from .models import Certificate

# Create your views here.

def resume(request):
    cer = Certificate.objects.all().first()
    return render(request,'resume/resume.html',{'education_flag':False,"cer":cer})
    # return HttpResponse("<h1>Resume</h2>")


def resume_education(request):
    return render(request,'resume/resume.html',{'education_flag':True})
    # return HttpResponse("<h1>Resume</h2>")
