
from django.urls import path
from . import views


# control pass karne ke baad yahan aaye
# localhost:8000/explore/
# localhost:8000/explore/metal
urlpatterns = [

    path("",views.compass_search,name='compass_search'),
    # path("metal/",views.metal,name="metal")

]
