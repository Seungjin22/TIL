from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    print(articles)
    # print(type(articles))
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    print(title)
    content = request.POST.get('content')
    
    #1. 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2. 두번째 방법
    # article = Article(title=title, content=content)
    # article.save()

    #3. 세번째 방법
    Article.objects.create(title=title, content=content)


    return redirect('/articles/')

def detail(request, pk):
    pass