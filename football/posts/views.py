from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post, New, Tournament
# Create your views here.
from django.http import HttpResponse

User = get_user_model()

def index(request):    
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    news = New.objects.order_by('-pub_date')[:10]
    context = {'posts': posts,
               'news': news,
               }
    return render(request, template, context)


def post_detail(request, pk):    
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    news = New.objects.order_by('-pub_date')[:10]
    context = {'post': post,
               'news': news}
    return render(request, template, context)

def new_detail(request, pk):    
    template = 'posts/new_detail.html'
    news = New.objects.order_by('-pub_date')[:10]
    new = New.objects.get(pk=pk)
    context = {'new': new,
               'news': news}
    return render(request, template, context)

def tournament_list(request, slug):
    tournament = get_object_or_404(Tournament, slug=slug)    
    template = 'posts/tournament_list.html'
    posts = Post.objects.filter(tournament=tournament).order_by('-pub_date')[:10]
    news = New.objects.order_by('-pub_date')[:10]
    context = {'posts': posts,
               'tournament': tournament,
               'news': news}
    return render(request, template, context)

