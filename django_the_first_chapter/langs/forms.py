from django import forms
from .models import Lang


# class LangForm(forms.Form):
#     lang = forms.ModelChoiceField(
# 		queryset=Lang.objects.all(),
# 		label="Select lang"
# 	)
    
    
class LangForm(forms.Form):
    lang = forms.ModelChoiceField(
        queryset=Lang.objects.all(),
        label="Select Language",
        widget=forms.Select(
            attrs={
                "class": "w-full text-black border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-sky-500 focus:outline-none"
            }
        )
    )