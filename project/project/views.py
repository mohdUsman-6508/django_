from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("<h1>This is home</h1>")
  return render(request,"index.html")