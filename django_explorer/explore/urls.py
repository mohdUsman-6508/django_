
from django.urls import path
from . import views


# control pass karne ke baad yahan aaye
# localhost:8000/explore/
# localhost:8000/explore/metal
urlpatterns = [

    path("",views.compass_search,name='compass_search'),
    # path("metal/",views.metal,name="metal")
    path('<int:chai_id>',views.chai_detail,name='chai_detail'),

]
