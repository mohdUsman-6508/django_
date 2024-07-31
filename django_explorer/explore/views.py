from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import  get_object_or_404
# Create your views here.

def compass_search(request):
  chais=ChaiVariety.objects.all()
  # model se value le kar frontend me pass karni he 
  return render(request,"explore/compass.html",{'chais':chais})
  # {'chais':chais} bhej rahe

def chai_detail(request,chai_id):
  chai=get_object_or_404(ChaiVariety,pk=chai_id)
  return render(request,'explore/details.html',{'chai':chai})
