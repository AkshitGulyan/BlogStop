from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

class Blogview(ListView):
    model = Post
    template_name = 'blog/blog.html'

class Detailedview(DetailView):
    model=Post
    template_name = 'blog/blogdetail.html'
    
class AddPostView(CreateView):
    model = Post
    template_name = 'blog/addpost.html'
    fields = "__all__"
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = "blog/updateblog.html"
    fields = ['title', 'body']
