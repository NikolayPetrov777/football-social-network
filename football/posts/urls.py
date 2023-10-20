from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name ='index'),
    path('post/<int:pk>/', views.post_detail, name ='post_detail'),
    path('new/<int:pk>/', views.new_detail, name ='new_detail'),
    path('tournament/<slug:slug>/', views.tournament_list, name ='tournament_list'),
    # path('posts/', views.post_list),
    # path('post/<int:pk>/', views.post_detail),
    # path('group/<slug:slug>/', views.group_posts),
]
