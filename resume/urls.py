from django.urls import path,include
from . import views


app_name = 'resume'
urlpatterns = [
    path('', views.resume, name="resume"),
    path('education', views.resume_education, name="resume_education"),
]