from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name ='index'),
    # path('posts/', views.post_list),
    # path('post/<int:pk>/', views.post_detail),
    # path('group/<slug:slug>/', views.group_posts),
]
