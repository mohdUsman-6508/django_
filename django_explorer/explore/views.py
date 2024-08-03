from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import  get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.

def compass_search(request):
  chais=ChaiVariety.objects.all()
  # model se value le kar frontend me pass karni he 
  return render(request,"explore/compass.html",{'chais':chais})
  # {'chais':chais} bhej rahe

def chai_detail(request,chai_id):
  chai=get_object_or_404(ChaiVariety,pk=chai_id)
  return render(request,'explore/details.html',{'chai':chai})


def chai_store_view(request):
  stores=None
  if request.method=='POST':
    form=ChaiVarietyForm(request.POST)

    if form.is_valid():
      chai_variety=form.cleaned_data['chai_variety']
      stores=Store.objects.filter(chai_varieties=chai_variety)
  else:
    form=ChaiVarietyForm()

  return render(request,'explore/chai_stores.html',{'stores':stores,'form':form})




    


