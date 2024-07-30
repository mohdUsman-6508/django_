from django.http import HttpResponse
# templates load 
from django.shortcuts import render


def home(request):
  # return HttpResponse("You are at Django Explorer Home Page")
  return render(request,'website/index.html')

def about(request):
  # return HttpResponse("You are at about page")
  return render(request,'website/about.html')

def contact(request):
  # return HttpResponse("You are at contact page")
  return render(request,'website/contact.html')

















