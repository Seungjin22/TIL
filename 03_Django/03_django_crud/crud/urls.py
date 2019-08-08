from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls), #이건 프로젝트 urls.py에만 필요
]
