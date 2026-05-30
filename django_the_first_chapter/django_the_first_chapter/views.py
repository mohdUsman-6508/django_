from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # content = "Hello!, This is home page"
  # return HttpResponse(content)
  return render(request,'website/index.html')


def about(request):
  # content = "Hello!, This is about page"
  # return HttpResponse(content)
  return render(request,'website/about.html')


def contact(request):
  # content = "Hello!, This is contact page"
  # return HttpResponse(content)
  return render(request,'website/contact.html')
  



