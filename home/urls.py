from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('info/<id>/',infoview),
   
    path('admin/', admin.site.urls),
]
