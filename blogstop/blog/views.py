from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Blogview(ListView):
    model = Post
    template_name = 'blog/blog.html'

class Detailedview(DetailView):
    model=Post
    template_name = 'blog/blogdetail.html'