from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # GET
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # GET(new), POST(create)
    path('<int:pk>/', views.detail, name='detail'), # GET
    path('<int:pk>/delete/', views.delete, name='delete'), # POST
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'), # GET(edit), POST(update)
]