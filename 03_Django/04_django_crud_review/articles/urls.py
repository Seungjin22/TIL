from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # GET
    # path('new/', views.new),
    path('create/', views.create, name='create'), # GET(new), POST(create)
    path('<int:article_pk>/', views.detail, name='detail'), # GET
    path('<int:article_pk>/delete/', views.delete, name='delete'), # POST
    # path('<int:pk>/edit/', views.edit),
    path('<int:article_pk>/update/', views.update, name='update'), # GET(edit), POST(update)
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'), # POST
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'), # POST
]