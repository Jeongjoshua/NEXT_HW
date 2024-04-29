from django.urls import path
from . import views
urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.home, name='home'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('update/<int:article_id>/', views.update, name='update'),
    path('delete/<int:article_id>/', views.delete, name='delete'),
    path('delete-comment/<int:article_id>/<int:comment_pk>/', views.delete_comment, name='delete-comment'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),

]