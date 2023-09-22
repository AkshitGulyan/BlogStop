from django.contrib import admin
from django.urls import path
from .views import Blogview 

urlpatterns = [
    path("/blog", Blogview.as_view(), name="blog")
]