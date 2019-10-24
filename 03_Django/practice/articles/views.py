from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article, }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        article = article_form.save()
        return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {'article_form': article_form, }
    return render(request, 'articles/forms.html', context)


def delete(request, article_pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return redirect('articles:index')


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        article_form.save()
        return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {'article_form': article_form, }
    return render(request, 'articles/forms.html', context)


def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment = comment_form.save(commit=False)
        comment.article_id = article.pk
        comment.save()
        return redirect('articles:detail', article.pk)
    else:
        comment_form = CommentForm()
    context = {'comment_form': comment_form, }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)