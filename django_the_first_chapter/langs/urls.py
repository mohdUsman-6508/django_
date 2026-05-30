from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.langs,name='langs'),
    path('<int:lang_id>/',views.lang_detail,name="lang_detail"),
    path('lang_form/',views.lang_form,name="lang_form")
]
