# Django



Versatile 다용도의

Secure 안전한

Scalable 확장성 있는

Complete 완결성 있는

Maintainable 쉬운 유지보수

Portable 포터블한



django 성격

**Opinionated 독선적**  >  Unopinionated 관용적

다소 독선적. but 관용적인 면도 있음

약간 힙한 친구... 예아~ 마이웨이~

ex) 공식 문서가 정말 잘되어 있음

'django built-in template tags and filters' 참고



프레임워크 사용은 마치 프랜차이즈 카페 창업하는 것과 유사

우리는 프레임워크를 사용할 것이다!

python의 프레임워크 django



MVC (Model View Controller)

#### MTV (Model Template View) ==> django

M: 데이터를 관리

**T: 사용자가 보는 화면**

**V: 중간 관리자**

==> 우선 T & V 만 먼저!



---



1. 가상환경할 폴더에서 시작

   `python -m venv venv`

2. 그 다음 활성화시키기 위해

   `source venv/Scripts/activate`

3. 확인하기 위해 

   `pip list`

4. 프로젝트 생성

   `django-admin startproject django_intro .`

5. 앱 생성

   `python manage.py startapp 이름`

   

---



고유한 가상환경을 만들어서 제공

```python
student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ source venv/Scripts/activate
(venv)
```

프로젝트 시작시 이것부터!

```python
student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ django-admin startproject django_intro .
(venv)
```



```python
student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ python manage.py runserver
```



**settings.py** : 기본적 프로그램 셋팅과 관련된 모든 게 담겨있음

**urls.py**

==> 이 두 가지 파일이 중요



★ views.py  짱짱 중요!!!



app이 만들어지면 출생신고 해야지~

프로젝트(django_intro)에서 settings.py에서 INSTALLED_APPS 안에 써주면 끄읕



.py 3대장

models.py

views.py

urls.py



render(request, 'dinner.html', {'pick': pick})

render의 세 번째 자리!

1. 옵셔널 하다. (넘겨주면 그 html 파일에서 사용할 수 있음)
2. 딕셔너리 형태다.



for문을 쓸 때 꼭!!! 끝맺음 필요! 종료조건 미리 만들어놓고 내부 logic 작성하도록!!!!!!!!!☆★

```django
<h3>1. 반복문</h3>
{% for menu in menus %}
{% endfor %}
```

```django
<h3>2. 조건문</h3>
{% if '짜장면' in menus %}
{% endif %}
```





```html
<form action="/isbirth/">  ==> ""여기에 url.py안의 주소 넣어주기
    <input type="text">
    <input type="submit">
</form>
      
```





#### ★내가 주소창에 엔터를 치면서 일어나는 일★

가장 먼저 urls.py로 가서 'ping/'이라는 주소가 있는지 확인 -> views.py로 가서 함수 확인 -> ping.html로 가기

-> 어디로 어떤 박스에 넣어서 보낼건지! 정하고 -> urls.py로 가서 '/pong'이라는 주소 확인

-> views.py로 가서 함수 확인 후 -> pong.html로 가기

```python
# url.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]

```

```python
# views.py

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    word = request.GET.get('word')
    context = {
        'word': word,
    }
    return render(request, 'pong.html', context)
```

```html
<!-- ping.html -->

<form action="/pong/" method="GET">
    핑!: <input type="text" name="word">
    <input type="submit">
</form>
```

```html
<!-- pong.html -->

<h1>Ping-Pong : {{ word }}</h1>
```

```html
<!-- p탭 안에서는 아무리 Enter 쳐도 띄어쓰기 적용 X -->
<p>
    하하
     ㅎ하하하하
    하하하
    하하
</p>

<!-- pre 탭 사용해야!! -->
<pre>
	하하
	ㅎ
	하하하하
</pre>
```



​	< Form tag에서 중요한 두 가지 >

1. input 속성 (type은 디폴트, 중요한건 name='' 어떤 상자에 넣을 것인지)

   `<input type="text" name="box">` 

2. 메서드(GET 요청이 디폴트)

   1. GET
      - 데이터 조작 X,  ONLY 조회
      - 주소창에 query ? 식으로 나옴
   2. POST
      - 데이터 조작 가해짐 ㅇㅇ
      - 아무것도 나오지 않음 (body에 포함되어...)
      - ★ `csrf_token` 필수!! ★



get 요청은 데이터 조작이 가해지는가? ==> No!!!

post는 다름! 데이터에 조작 가해짐ㅇㅇ



#### Form - POST

`csrf_token`은 POST 보내기 방식에서 필수!!!

'내가 요청하는게 맞아~'라고 신원확인 해주는 것!

```python
# views.py

def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'user_create.html', context)
```

```python
# urls.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]

```

```html
<!-- user_new.html -->

<form action="/user_create/" method="POST">
    {% csrf_token %} <!-- Cross Site Request Forgery 토큰 필수! -->
    이름: <input type="text" name="name">
    비밀번호: <input type="password" name="pwd">
    <input type="submit">
</form>
```

```html
<!-- user_create.html -->

<p>이름: {{ name }}</p>
<p>비밀번호: {{ password }}</p>
```



템플릿 확장







VS Code

code . 은 씹히는 현상 발생...!

open with code(오른쪽 마우스) 로 열면 괜춘!!



## 데이터베이스(DB)

: **체계화된** 데이터의 모임

​	몇 개의 자료 파일을 조직적으로 모아둔 것



RDBMS(관계형데이터베이스 관리 시스템)

관계형 모델을 기반으로 하는 데이터베이스 관리시스템

- SQLite
  - 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 DB



< 데이터베이스 용어 >

- 스키마

  : 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조.

- 테이블(table)

  : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합. (엑셀 sheet와 유사)

    SQL 데이터베이스에서는 테이블을 관계라고도 함.

- 열(column)

  : 각 열에는 고유한 데이터 형식이 지정된다. ex) INTEGER, TEXT, NULL 등

- 행(row), 레코드

  : 테이블의 데이터는 행에 저장.

- PK(기본키)

  : 각 행(레코드)의 고유값으로 Primary Key로 불림.

    반드시 설정해야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용됨.



SQL(Structured Query Language)

: 관계형 데이터베이스 관리시스템의 데이터 관리하기 위해 설계된 특수 목적의 프로그래밍 언어



ORM

CRUD (Create Read Update Delete)



|     SQL     |  CRUD  |
| :---------: | :----: |
|   SELECT    |  READ  |
| INSERT INTO | CREATE |
|   UPDATE    | UPDATE |
|   DELETE    | DELETE |



파이썬은 모든 것이 객체...

DB의 행, 테이블도 객체화 해볼 수 있지 않을까?

==> ORM(Object-Relational Mapping)

ORM은 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간(Django - SQL)에 데이터를 변환하는 프로그래밍 기술





make migrations 까지는 DB에 적용되지 않은 상태!

=> 설계도를 만들고 이거 맞아? 물어보는 단계!



```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) # 제목 너무 길어지지 않도록
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

auto_now_add

auto_now

헷갈리기 딱 좋음



####    ★ 3 단계 ★

1. ##### models.py에 테이블 정의한다.

2. ##### make migrations을 통해 설계도를 만든다. ==> 앱 등록!!!!!!!!!! 잊지말아유~

   `$ python manage.py makemigrations`

3. ##### migrate를 통해 데이터베이스에 반영한다.

   `$ python manage.py migrate`



---



### Django shell



​	쉘에 접근하는 방법

​    `$ python manage.py shell`

​	쉘 종료 : `exit()`



```
$ python manage.py shell
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from articles.models import Article
>>> Article.objects.all()			==> 나 이거 좀 다 주세요! objects는 번역기같은 존재
<QuerySet []>						==> 아직 아무것도 없는 상태 (빈 DB)

# .all()은 아무것도 없는 상태에도 빈 QuerySet [] 보여줌

>>> article = Article()				==> 방법(1) 따로따로!  인스턴스 생성
>>> article.title = 'first'
>>> article.content = 'django!'
>>> article
<Article: Article object (None)>
>>> article.save()					==> save 해줘야!!!! 값이 들어감
>>> article
<Article: Article object (1)>
>>> article.title
'first'
>>> article.content
'django!'
>>> article.created_at
datetime.datetime(2019, 8, 7, 7, 9, 45, 890128, tzinfo=<UTC>)

>>> article = Article(title='second', content='django!') ==> 방법(2) 한 번에 주룩~
>>> article
<Article: Article object (None)>
>>> article.save()
>>> article
<Article: Article object (2)>
>>> article.title
'second'
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>

>>> Article.objects.create(title='third', content='django!') ==> 방법(3) save까지 한 번에!!
<Article: Article object (3)>
```

근데 상태가 너무 마음에 안들잖아~

사람이 보기 힘들어!! ㅠㅠ

==> `__str__` 매직 메서드 사용해보자! 우리가 보기 편하게!

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) # 제목 너무 길어지지 않도록
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'
```

```
$  python manage.py shell
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from articles.models import Article		==> shell 새로 켤 때마다 불러오기! 잊지마유~
>>> articles = Article.objects.all()
>>> articles
<QuerySet [<Article: 1번 글 - first: django!>, <Article: 2번 글 - second: django!>, <Article: 3번 글 - third: django!>, <Article: 4번 글 - fourth: django!>]>


>>> type(articles)
<class 'django.db.models.query.QuerySet'>		==> 얘는 QuerySet 리스트처럼 생긴...


>>> Article.objects.create(title='first', content='hahaha')
<Article: 5번 글 - first: hahaha>
>>> articles = Article.objects.filter(title='first')	==> .filter(필터링 조건)
>>> articles
<QuerySet [<Article: 1번 글 - first: django!>, <Article: 5번 글 - first: hahaha>]>


>>> Article.objects.create(title = 'first', content = 'vacation')
<Article: 6번 글 - first: vacation>
>>> article = Article.objects.filter(title='first').first()
											==> 메서드 체이닝(Method Chaining)
>>> article
<Article: 1번 글 - first: django!>			==> first()랑 last()만 가능!!!
>>> article = Article.objects.filter(title='first').last()
>>> article
<Article: 6번 글 - first: vacation>

>>> Article.objects.get(pk=3)		==> .get() 사용해서 pk가 3인 값 가져오기
<Article: 3번 글 - third: django!>

>>> Article.objects.get(title='first')  ==> title='first'인게 3개가 있어!!! ERROR-_-
Traceback (most recent call last):				.get()은 무조건 하나인 걸로! (primary key)
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 412, in get
    (self.model._meta.object_name, num)
articles.models.Article.MultipleObjectsReturned: get() returned more than one Article -- it returned 3!


>>> Article.objects.get(pk=10)		==> 없는 경우 가져올때, 필터 사용하면 에러 X
Traceback (most recent call last):	   => .get()의 경우 지금처럼 에러!(무조건 하나인 값 넣기)
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 408, in get
    self.model._meta.object_name
articles.models.Article.DoesNotExist: Article matching query does not exist.

>>> Article.objects.filter(pk=10)	==> .filter()의 경우에는 에러 없음
<QuerySet []>						무조건 return이 있어야!!! 몇 개인지 보장 불가능(by.ORM)


>>> Article.objects.all()[2]	==> QuerySet은 리스트 형태. 인덱스 호출 가능
<Article: 3번 글 - third: django!>
>>> articles = Article.objects.all()[1:3]	==> 슬라이싱!
>>> articles
<QuerySet [<Article: 2번 글 - second: django!>, <Article: 3번 글 - third: django!>]>
```

article = Article.objects.filter(title__contains='fir')

articles = Article.objects.filter(title__startswith='first')

articles = Article.objects.filter(title__endswith='first')



article = Article.objects.get(pk=1)

article.title = 'byebye'

article.save()

article

<Article: 1번 글 - byebye: django!>



article.delete()

Article.objects.delete



admin 들어가려면 관리자 계정 필요

`$ python manage.py createsuperuser`





settings.py에서 INSTALLED_APPS = []에 앱 출생 신고 해줄때

원래 맨 위에 추가해줬는데

() 경우에는 마지막에 넣어주는 것이 convention



`$ python manage.py shell_plus`



---



만들고

`$ python -m venv venv`

실행하고

`$ source venv/Scripts/activate
(venv)` 

django 설치

`$ pip install django`

프로젝트 만들기

`$ django-admin startproject crud .`

앱 만들기

`$ python manage.py startapp articles`

==> ★ 앱 출생신고!!! 잊지마!!!



---



```python
# urls.py

from django.contrib import admin
from django.urls import path, include # include 중요해~

urlpatterns = [
    path('articles/', include('articles.urls')),	# include 잊지마!!!
    path('admin/', admin.site.urls),
]
```



``` python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],	==> 이 부분!!!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



```python
# models.py

from django.db import models

class Article(models.Model):  ==> 항상 models.Model을 상속받음
    title = models.CharField(max_length=20) #필수 인자 max_length=숫자
    content = models.TextField()    #필수 인자 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
    	return f'{self.id}번 글 - {self.title}: {self.content}'
```



데이터 베이스 상에서 그 순서로 불러오는 것(정렬해서 줘~)

`articles = Article.objects.order_by('-id')`

일단 다 가져온 후 파이썬 코드로 돌려서 다시 슬라이싱 하는 것

`articles = Article.objects.all()[::-1]`



---



모델 정의하기

```python
# models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20) #필수 인자 max_length=숫자
    content = models.TextField()    #필수 인자 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'
```

`$ python manage.py makemigrations`

`$ python manage.py migrate`



```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]
```



```python
# views.py

from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    #방법 (1)
    article = Article()
    article.title = title
    article.content = content
    article.save()
    
    #방법 (2)
    #article = Article(title=title, content=content)
    #article.save()

    return redirect('/articles/')
```



```html
<!-- index.html -->

{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">Articles</h1>
<hr>
{% for article in articles %}
    <p>글 번호: {{ article.id }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
{% endfor %}
<a href="/articles/new/"> [글쓰기]</a>
{% endblock %}
```

타겟 태그!!!!! 추가해서 새 탭으로 열기 해보기~

```html
<!-- new.html -->

{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">NEW PAGE</h1>
<form action="/articles/create/" method="POST">
    {% csrf_token %}
    <label for="title">Title</label><br>
    <input type="text" id="title" name="title"><br>
    <label for="content">Content</label><br>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
    <input type="submit" value="글쓰기">
</form>
<a href="/article/" target="_self">뒤로 ←</a>
{% endblock %
```





views.py 윗부분

from .models import Article

.models 대신에 . 을 쓰면 어떨까? / 안돼~ from까지가 ~에서 가져온다고 생각해.



```python
# admin.py

from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

==> admin.py에 이렇게 등록해줘야 서버에 뜸



---

글 하나하나 띄우기(R) / 삭제(D) / 수정(U)

detail은 하나하나 세부적인 글 보여주기 위해 필요했음

edit 으로 보낸 후 수정한걸 update로 보내줘야!

` <a href="/articles/{{ article.pk }}/edit/" target="_blank">[글 수정]</a>`

target="_blank"











<ul class="navbar-nav mr-auto">

​            <li class="nav-item active">

​              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>

​            </li>

​            <li class="nav-item">

​              <a class="nav-link" href="#">친구 평점 보러가기</a>

​            </li>

​            <li class="nav-item">

​                <a class="nav-link" href="#">Log In</a>

​            </li>







 class="d-flex justify-content-center align-items-center"