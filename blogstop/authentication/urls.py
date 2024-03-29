from django.contrib import admin
from django.urls import include, path
from . import views
from blog.views import AddPostView, Detailedview

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    # path('addpost', AddPostView.as_view(), name='add_post'),
    # path('article/<int:pk>', Detailedview.as_view(), name='article'),
]