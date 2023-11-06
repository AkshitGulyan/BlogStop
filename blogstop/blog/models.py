from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)  
    
    def get_absolute_url(self):
        # print(type(self.id))
        a=str(self.pk)
        # print(a)
        # print(type(a))
        return reverse('article',args={a})
    
