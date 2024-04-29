from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from datetime import datetime
from django.contrib.auth.decorators import login_required
from authapp.permissions import check_is_creator_or_admin
from .decorators import update_last_viewed
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
@login_required
def new(request):
    if request.method == 'POST':
        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            time = datetime.now(),
            creator = request.user
        )
        return redirect(reverse('home'))
    
    return render(request, 'new.html')

def home(request):
    articles = Article.objects.all()

    return render(request, 'home.html', {'articles': articles})

@login_required
@update_last_viewed
def detail(request, article_id):
    article = Article.objects.get(pk =article_id)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
         article = article,
         content = content,
         creator = request.user
        )
        return redirect('detail', article_id)
    
    return render(request, 'detail.html', {'article': article})


@login_required
@check_is_creator_or_admin(Article, "article_id")
def update(request, article_id):
    article = Article.objects.get(pk = article_id)

    if request.method == 'POST':
        Article.objects.filter(pk=article_id).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', article_id)
    
    return render(request, 'update.html', {'article': article})

@login_required
@check_is_creator_or_admin(Article, "article_id")
def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()

    return redirect(reverse('home'))

@login_required
@check_is_creator_or_admin(Comment, "comment_pk")
def delete_comment(request, article_id, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()

   return redirect('detail',article_id)

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(creator=user)

    return render(request, 'user_profile.html', {'user_profile': user} )



