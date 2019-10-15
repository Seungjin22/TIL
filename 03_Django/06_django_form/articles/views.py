from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채움
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            # form.cleaned_data를 통해 폼 데이터를 정제 (type(form.cleaned_data) = dict)
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form, }
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article, }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index') # redirect ==> GET
    return redirect('articles:detail', article.pk)