from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone 
from django.utils.timezone import activate
from pytz import timezone as tz


def home(request):
    posts = Post.objects.all()
    blog_count = Post.objects.count()
    hobby_count = Post.objects.filter(category='hobby').count()
    food_count = Post.objects.filter(category='food').count()
    programming_count = Post.objects.filter(category='programming').count()
    return render(request, 'home.html', {'posts': posts, 'blog_count' : blog_count, 'hobby_count': hobby_count, 'food_count': food_count, 'programming_count': programming_count})

def new(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
            published_date = timezone.now(),
        
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
        post.category = request.POST['category']  
        activate(tz('Asia/Seoul'))
        post.published_date = timezone.now()
        return redirect('detail', post_pk)
    
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def posts_by_category(request, category):
    posts = Post.objects.filter(category=category)
    
    return render(request, 'posts_by_category.html', {'category': category, 'posts': posts})

