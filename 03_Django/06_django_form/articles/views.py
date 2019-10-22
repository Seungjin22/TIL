from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http  import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
import hashlib
from IPython import embed

def index(request):
    #1. session 정보에서 visits_num 이라는 키로 접근해 값을 가져옴
    visits_num = request.session.get('visits_num', 0) # 해당 값이 없으면 0 가져옴

    #2. 가져온 값을 session에 'visits_num' 이라는 새로운 키의 값으로 1씩 증가
    request.session['visits_num'] = visits_num + 1
    #3. session data를 수정하면 장고는 수정한 내용을 알 수 없어서 작성하는 구문
    request.session.modified = True
    # embed()
    articles = Article.objects.all()
    context = {'articles': articles, 'visits_num': visits_num, }
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    """
    Form Class
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 데이터 정제 후
    DB에 실제 저장하는 로직 필요

    Model Form
    이미 Model에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고
    form.save()만 해도 DB에 저장됨
    """
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채움
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            article = form.save(commit=False)
            article.user_id = request.user.id
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form, }
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    comment_form = CommentForm(request.POST)
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
    return redirect('articles:index') # redirect ==> GET


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article) # 사용자가 입력한 값을 초기값으로 넘겨줌
    else:
        return redirect('articles:index')
    context = {'form': form, 'article': article, }
    return render(request, 'articles/form.html', context)

"""
* CREATE & UPDATE는 html 파일 공유

Creat 로직
1. GET
- 사용자가 데이터를 입력할 수 있는 빈 Form을 제공
2. POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1. GET
- 기존 사용자의 글이 입력된 Form 제공
2. POST
- 수정된 글을 DB에 저장
"""

@require_POST
def comments_create(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    # if request.method == 'POST':
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user_id = request.user.id
            comment.save()
    return redirect('articles:detail', article_pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


def comments_update(request, article_pk, comment_pk):
    if request.method =='POST':
        article = get_object_or_404(Article, pk=article_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('articles:detail', article.pk)
    else:
        comment_form = CommentForm(instance=comment) # 사용자가 입력한 값을 초기값으로 넘겨줌
    context = {'comment_form': comment_form, 'article': article, 'comment': comment, }
    return render(request, 'articles/detail.html', context)
