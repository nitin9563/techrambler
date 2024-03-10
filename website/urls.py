from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("add/",views.dataadd),
    path("code/<str:id>",views.code)
]