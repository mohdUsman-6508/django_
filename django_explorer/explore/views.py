from django.shortcuts import render

# Create your views here.

def compass_search(request):
  return render(request,"explore/compass.html")
