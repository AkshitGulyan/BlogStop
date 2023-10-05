from django.contrib import admin
from django.urls import path
from .views import Blogview , Detailedview
from authentication import views


urlpatterns = [
    path("blog", Blogview.as_view(), name="blog"),
    path('article/<int:pk>', Detailedview.as_view(), name='article'),
    path("blog", Blogview.as_view(), name="blog"),
    path('index', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),


]