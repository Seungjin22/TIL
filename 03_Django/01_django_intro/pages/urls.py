from django.urls import path
from . import views          # . 은 현재 디렉토리


urlpatterns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/', views.ispal),
    path('isbirth/', views.isbirth),
    path('template_language/', views.template_language),
    path('area/<int:r>', views.area),
    path('multi/<int:num1>/<int:num2>/', views.multi),
    path('aboutme/<name>/<int:age>/', views.aboutme),
    path('hello/<name>/<int:age>/', views.hello), # <>안은 변수가 됨 default가 str
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]