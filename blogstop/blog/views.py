from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse

class Blogview(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-id']

class Detailedview(DetailView):
    model=Post
    template_name = 'blog/blogdetail.html'
    context_object_name = 'post'    
class AddPostView(CreateView):
    model = Post
    template_name = 'blog/addpost.html'
    fields = "__all__"
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = "blog/updateblog.html"
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model= Post
    template_name = "blog/deleteblog.html"
    success_url = reverse_lazy('blog')