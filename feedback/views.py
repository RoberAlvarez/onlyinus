from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

def home(request):
    sort = request.GET.get('sort', 'new')
    if sort == 'top':
        posts = Post.objects.order_by('-votes', '-created_at')
    else:
        posts = Post.objects.order_by('-created_at')
    voted_ids = []
    for post in posts:
        if request.COOKIES.get(f'voted_post_{post.id}'):
            voted_ids.append(post.id)
    return render(request, 'feedback/home.html', {
        'posts': posts,
        'voted_ids': voted_ids,
        'sort': sort,
    })

def submit_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return redirect('view_post', post_id=post.id)
    return render(request, 'feedback/submit.html', {'form': form})

def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    cookie_name = f'voted_post_{post_id}'
    if request.COOKIES.get(cookie_name):
        return redirect('home')
    post.votes += 1
    post.save()
    response = redirect('home')
    response.set_cookie(cookie_name, "1", max_age=60*60*24*365*2)
    return response


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.order_by('-created_at')
    voted = request.COOKIES.get(f'voted_post_{post_id}')
    comment_likes = []
    for comment in comments:
        if request.COOKIES.get(f'liked_comment_{comment.id}'):
            comment_likes.append(comment.id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('view_post', post_id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'feedback/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'voted': voted,
        'comment_likes': comment_likes,
    })

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    cookie_name = f'liked_comment_{comment_id}'
    if request.COOKIES.get(cookie_name):
        return redirect('view_post', post_id=comment.post.id)
    comment.likes += 1
    comment.save()
    response = redirect('view_post', post_id=comment.post.id)
    response.set_cookie(cookie_name, "1", max_age=60*60*24*365*2)
    return response
