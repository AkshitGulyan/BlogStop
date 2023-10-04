from django.contrib import admin
from django.urls import path
from .views import Blogview , Detailedview

urlpatterns = [
    path("blog", Blogview.as_view(), name="blog"),
    path('article/<int:pk>', Detailedview.as_view(), name='article'),
]