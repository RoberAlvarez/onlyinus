from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_post, name='submit'),
    path('upvote/<int:post_id>/', views.upvote_post, name='upvote'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]
