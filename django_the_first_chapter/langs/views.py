from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Lang,Enterprise
from .forms import LangForm

# Create your views here.

def langs(request):
  langs = Lang.objects.all()
  return render(request,'langs/all_langs.html',{'langs':langs})


def lang_detail(request,lang_id):
 lang= get_object_or_404(Lang,pk=lang_id)
 return render(request,'langs/lang_details.html',{'lang':lang} )


def lang_form(request):
  
  enterprises = None
  if request.method == 'POST':
    form = LangForm(request.POST)
    if form.is_valid():
      lang = form.cleaned_data['lang']
      enterprises = Enterprise.objects.filter(langs=lang)
  else:
    form=LangForm()
        
  return render(request,'langs/lang_form.html',{'form':form,'enterprises':enterprises})
  
  