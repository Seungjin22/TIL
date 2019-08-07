from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # 인덱스는 뒷 주소 달지 않음
    path('mamago/', views.mamago),
    path('translated/', views.translated),
]