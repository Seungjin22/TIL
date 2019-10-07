from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # GET
    # path('new/', views.new),
    path('create/', views.create), # GET(new), POST(create)
    path('<int:pk>/', views.detail), # GET
    path('<int:pk>/delete/', views.delete), # POST
    # path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update), # GET(edit), POST(update)
]