"""
URL configuration for django_explorer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# static method ko batana padta he ki setting me se mediaurl ko load kar le

urlpatterns = [
  
  
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    # jab bhi explore ka url hit kare to control transfer kar de explore.urls par(jo alag alag app hum bana rahe)
    path("explore/",include('explore.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# abhi tak django ko pata nahin he ki hum ne model add kiye he
# use batane ke liye 2 command lagegi - "makemigrations","migrate"

