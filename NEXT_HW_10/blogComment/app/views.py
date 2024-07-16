from django.shortcuts import render, redirect
from .models import Post, Comment, Reply
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
    
    if request.method == 'POST':
        if 'content' in request.POST:
            # If 'content' is in request.POST, it's a comment
            content = request.POST['content']
            Comment.objects.create(
                post=post,
                content=content
            )
        elif 'reply_content' in request.POST:
            # If 'reply_content' is in request.POST, it's a reply
            reply_content = request.POST['reply_content']
            comment_id = request.POST['comment_id']  # assuming this is passed as hidden input in the form
            comment = Comment.objects.get(pk=comment_id)
            Reply.objects.create(
                comment=comment,
                content=reply_content
            )
        return redirect('detail', post_pk)

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

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail',post_pk)

def delete_reply(request, post_pk, comment_pk, reply_pk):
   reply = Reply.objects.get(pk=reply_pk)
   reply.delete()
   return redirect('detail', post_pk)