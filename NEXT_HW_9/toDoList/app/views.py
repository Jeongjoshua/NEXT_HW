from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone 
from django.utils.timezone import activate
from pytz import timezone as tz


# Create your views here.
def home(request):
    # Get all Post objects
    posts = Post.objects.all()

    for post in posts:
        post.days_left = post.get_days_left()
    
    posts = sorted(posts, key=lambda x: (
        0 if x.days_left == "D-Day" else (-1 if x.days_left.startswith("D-") else 1),
        x.days_left))

    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            selected_date=request.POST['due_date'],  
        )
        return redirect('home')
    return render(request, "new.html")
    
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.selected_date = request.POST['due_date']
        post.save()
    
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

