from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments_create', views.comments_create, name='comments_create'),
    path('<int:article_pk>/<int:comment_pk>/comments_delete', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/<int:comment_pk>/comments_update', views.comments_update, name='comments_update'),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/follow/<int:user_pk>/', views.follow, name='follow'),
]