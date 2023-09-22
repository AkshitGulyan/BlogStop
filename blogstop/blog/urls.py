from django.contrib import admin
from .views import Blogview

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.home, name='home'),
]