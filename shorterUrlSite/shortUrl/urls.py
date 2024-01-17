from django.contrib import admin
from django.urls import path 
from shortUrl.views import *

urlpatterns = [
    path('', Main.as_view())   
]
