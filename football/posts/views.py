from django.shortcuts import render
from .models import Post, New
# Create your views here.
from django.http import HttpResponse

def index(request):    
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    news = New.objects.order_by('-pub_date')[:10]
    context = {'posts': posts,
               'news': news}
    return render(request, template, context)
