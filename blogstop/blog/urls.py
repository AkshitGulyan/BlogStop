from django.contrib import admin
from django.urls import path
from .views import Blogview , Detailedview
from authentication import views


urlpatterns = [
    path("blog", Blogview.as_view(), name="blog"),
    path('article/<int:pk>', Detailedview.as_view(), name='article'),
    path("article/blog", Blogview.as_view(), name="blog"),
    path('article/index', views.home, name='home'),
    path('article/signup', views.signup, name='signup'),
    path('article/signin', views.signin, name='signin'),
    path('article/signout', views.signout, name='signout'),
    path('article/about', views.about, name='about'),
    path('article/contact', views.contact, name='contact'),


]