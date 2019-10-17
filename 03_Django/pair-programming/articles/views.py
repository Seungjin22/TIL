from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.views.decorators.http import require_POST
import bootstrap4


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    # embed()
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        article = article_form.save()
        return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {'article_form': article_form, }
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comments.all()
    comment_form = CommentForm()
    context = {'article': article, 'comments': comments, 'comment_form': comment_form, }
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # article_form = ArticleForm(instance=article)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        article_form.save()
        return redirect('articles:detail', article_pk)
    # article_form = ArticleForm(Article, instance=article)
    else:
        article_form = ArticleForm(instance=article)
        context = {'article_form': article_form, 'article': article, }
        return render(request, 'articles/create.html', context)

@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def comments_create(request, article_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
        return redirect('articles:detail', article_pk)
    comment_form = CommentForm()
    context = {'comment_form':comment_form, }
    return render(request, 'articles/detail.html', context)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    