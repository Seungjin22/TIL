# Django



Dynamic Web



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

​	M: 데이터를 관리 (어떤 형태의 데이터인지 모델링)

​	**T: 사용자가 보는 화면**

​	**V: 중간 관리자**

==> 우선 T & V 만 먼저!

Model 데이터가 없으면 아무것도 할 수가 없음

Modeling 할 때 필요한 데이터 중요



---

- 가상환경을 쓰는 이유 : 의존성 문제 제거하기 위해서



1. 가상환경할 폴더에서 시작 (`venv`라는 가상환경을 `venv`라는 이름으로 사용하겠다)

   `python -m venv venv`

2. 그 다음 활성화시키기 위해

   `source venv/Scripts/activate`

3. 확인하기 위해 

   `pip list`

4. 프로젝트 생성

   `django-admin startproject django_intro .`

5. 앱 생성

   `python manage.py startapp 이름`

   
   
   가상환경 끄려면
   
   `deactivate`
   
   
   
   django 설치
   
   `pip install django`
   
   

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



app이 만들어지면 **출생신고** 해야지~ `settings.py`

프로젝트(django_intro)에서 settings.py에서 INSTALLED_APPS 안에 써주면 끄읕



##### .py 3대장

1. `models.py`

2. `views.py` : urls.py를 통해 요청이 들어오면 DB와 소통, template 뿌려주기 등 / 중간관리자 역할

3. `urls.py` : 어떤 경로에 views.py에서 정의한 함수를 이어줌





오리지널 urls.py(/crud) : 뿌려주는 애



앱 밑에 `templates` 만들기

```text
articles
	templates
		articles
```

==> name space 구분이 왜 중요한가?

​		directory가 다르면 네임 스페이스 구분. 인위적으로 구분해주는 것



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

가장 먼저 `urls.py`로 가서 'ping/'이라는 주소가 있는지 확인 ->`views.py`로 가서 함수 확인 -> ping.html로 가기

-> 어디로 어떤 박스에 넣어서 보낼건지! 정하고 -> `urls.py`로 가서 '/pong'이라는 주소 확인

-> `views.py`로 가서 함수 확인 후 -> pong.html로 가기

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

==> **ORM**(Object-Relational Mapping)

ORM은 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간(Django - SQL)에 데이터를 변환하는 프로그래밍 기술

##### 파이썬 class로 DB 조작이 가능하다!





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



​		`python manage.py sqlmigrate 모델이름 0001`

​		`python manage.py showmigrations`

> make migrations 까지는 DB에 적용되지 않은 상태!
>
> => 설계도를 만들고 이거 맞아? 물어보는 단계!

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



tag를 쓰는 이유 : DOM Tree 계층 구조

- render 함수 쓰는 이유 : html 파일을 사용자에게 보여주고자 할 때

- redirect 함수 쓰는 이유 : 일단 redirect 함수 첫 번째 인자로 **다시 한 번 요청을 보냄**

==> GET과 POST의 차이!



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
{% endblock %}
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







CDN Delivery Network



- app_name 왜 해줘요?

  : 경로에 대한 의존성 문제 해결하기 위해서 ( 경로 수정이 필요할 때 `urls.py`에서만 수정 가능하도록! )





---



### HTTP 기초

Hypertext Transfer Protocol

컨텐츠를 전송하기 위한 프로토콜(규약)



##### HTTP 기본 속성

|             |                                                              |
| ----------- | :----------------------------------------------------------- |
| Stateless   | 상태정보가 저장되지 않음. 즉, 요청 사이에는 연결고리가 없음. 클라이언트가 서버와 상호작용하기 위해서 HTTP 쿠키를 만들고, 상태가 있는 세션을 활용할 수 있도록 보완 |
| Connectless | 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐            |



#### URL

```text
Scheme/Protocol    Host    Port  
http    ://    localhost : 3000 / posts / 3

http://google.com/search?	q=http	==> query | URI는 맞지만 URL은 아니다.
http://getbootstrap.com/docs/	#containers  ==> fragment
```

Locator는 그 자리에 가면 그 자원이 있어야!



403 Forbidden ==> 토큰 깜빡하고 요청할때 발생하는 에러



#### HTTP Method

|   구분    |                          비고                          |
| :-------: | :----------------------------------------------------: |
|    GET    | 지정 리소스의 표시를 요청하며, 오직 데이터를 받기만 함 |
|   POST    |            클라이언트 데이터를 서버로 보냄             |
| PUT/PATCH | 서버로 보낸 데이터를 저장/지정 리소스의 부분만을 수정  |
|  DELETE   |                   지정 리소스를 삭제                   |



### RESTful (Representational State Transfer)

: 웹의 장점을 활용하는 것에 대한 철학(생각) / 자원과 행위를 잘 표현 하자는 철학(생각) or 설계



- 구성

| 자원 |    행위     |      표현       |
| :--: | :---------: | :-------------: |
| URI  | HTTP Method | Representations |



- 특징
  - Uniform
  - Stateless (무상태성)
  - Cacheable (캐시가능) : HTTP의 캐시 기능이 적용 가능함
  - Self-descriptiveness (자체표현구조) : REST API 메시지만 보고 상태와 행위
  - Client - Server 구조
  - 계층형 구조



#### REST 중심 규칙

1. **URI**는 정보의 **자원**을 표현해야 한다.
2. 자원에 대한 **행위**는 **HTTP Method** 로 표현한다.



GET/users/1/delete/ (X) ==>  URI는 자원을 표현하는데에만 중점을 둬야함 >> DELETE/users/1/

GET/users/1/create/ (X) ==> Method가 올바르지 않음 (create는 DB에 조작을 가함) >> POST/users/1/





`$ pip install django-extensions`

`$ pip install ipython`



```python
from IPython import embed

# 함수 안에서 embed()로 브레이크 걸어주기
embed()

>>>Terminal
In [1]: request
Out[1]: <WSGIRequest: POST '/articles/9/update/'>
        
In [2]: request.method
Out[2]: 'POST'
    
In [3]: request.body
Out[3]: b'csrfmiddlewaretoken=6PqHqXW0ramiB0HNv4AnRJiD4xVjVq6maQ1bxVbO5aSjNmj8hdNCtrIeE2nhpofN&title=%EB%91%98%EB%A6%AC%EA%B0%80123&content=%ED%98%B8%EC%9E%87%ED%98%B8%EC%9E%87123'
```



GET과 POST 형식 두 개 합치기





### Model Relation (1: N) | 댓글달기

`ForeignKey`는 N의 모델 안에서 설정

```python
# models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # on_delete
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-pk', ]
```

==> `on_delete=models.CASCADE` : 게시글 삭제하면 밑에 달린 댓글도 다 삭제



- **order_by** : DB 상에 insert한 순서대로 되어있을 때 그 순서 뒤집기

- **ordering** : order_by를 사용하지 않아도 그 순서가 바뀌어서 나옴 ('-pk' 순으로 자동 저장)





comments`.exclude()` <==> comments`.filter()`

`filter()` 는 없는 객체 소환해도 에러는 안 남. 빈 리스트 `<QuerySet []>`을 가져올 뿐

```python
In [13]: comments.exclude(content='first comment')
Out[13]: <QuerySet [<Comment: <Article(2): Comment(3 - third comment)>>, <Comment: <Article(2): Comment(2 - second comment)>>]>

In [14]: comments.filter(content='first comment')
Out[14]: <QuerySet [<Comment: <Article(2): Comment(1 - first comment)>>]>

In [15]: comments.filter(content='fifth content')
Out[15]: <QuerySet []>
```



```python
# .iterator()
In [18]: for comment in comments.iterator():
    ...:     print(comment)
    ...: 
<Article(2): Comment(3 - third comment)>
<Article(2): Comment(2 - second comment)>
<Article(2): Comment(1 - first comment)>

In [19]: for comment in comments:
    ...:     print(comment)
    ...: 
<Article(2): Comment(3 - third comment)>
<Article(2): Comment(2 - second comment)>
<Article(2): Comment(1 - first comment)>
```

메모리 캐시가 누수되는 걸 방지하기 위해 `iterator()` 사용





`article.comment` (X) 불가능 ==> 1(article)의 입장에서는 N(comment)을 가리킬 수 없음 (**보장**할 수 없음)

`article.comment_set.all()` (O)  전부 불러와줘야!

`comment.article` (O) 가능 ==> N의 입장에서 가리키는 1은 확실하니까 가능



`related_name` 을 설정하는 순간 `_set` 이 아닌 설정한 이름으로 1이 N을 불러올 수 있음!

>```python
># models.py에서 related_name 설정하기
>
>class Comment(models.Model):
>    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
>    content = models.CharField(max_length=30)
>    created_at = models.DateTimeField(auto_now_add=True)
>    updated_at = models.DateTimeField(auto_now=True)
>    
>    
># TERMINAL
>In [3]: article.comments.all()	# 이제 comment_set 사용 불가 ==> comments 가능
>Out[3]: <QuerySet [<Comment: <Article(2): Comment(3 - third comment)>>, <Comment: <Article(2): Comment(2 - second comment)>>, <Comment: <Article(2): Comment(1 - first comment)>>]>
>```





comment_pk 와 article_pk 구분해주기

`views.py` 에서 게시글 pk ==> article_pk 로 바꿔주기

`urls.py` 에서 게시글 pk ==> article_pk 로 바꿔주기



```html
<!-- detail.html -->

<h5>댓글 목록</h5><br>
    {% for comment in article.comments.all %}
        <p>댓글 번호 : {{ comment.pk }}</p>
        <p>댓글 내용: {{ comment.content }}</p>
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="댓글 삭제" class="btn btn-warning">
        </form><br>
    {% endfor %}
```





앱 아래 `static` 폴더 만들고 그 아래에 이름 공간 구분 `앱이름`

```text
articles(앱)
	static
		articles
			images
				disney.jpg
			
			
crud(프로젝트)
	assets
		images
			disneyland.jpg
```



`settings.py` 에서 설정

```python
# settings.py

# 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
# (주의! 실제 파일이 위치한 디렉토리는 아님)
STATIC_URL = '/static/'

# 정적 파일이 실제 위치한 경로
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'crud', 'assets'),
]
```

==> `STATICFILES_DIRS` 를 통해 assets 까지 경로를 Django에게 알려줬음

```html
<!-- disneyland.jpg 불러오려면 -->

{% static 'images/disneyland.jpg' %}

<!-- disney.jpg 불러오려면 -->

{% static 'articles/images/disney.jpg' %}
```



`models.py` 에서 DB에 image 넣기 위해 새 column 만들어주기

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True) # 이미지 없으면 '' 빈 스트링 들어감
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



`create.html` 에서 image 파일 업로드할 수 있는 부분 만들어주기

```html
<label for="image">Image</label>
<input type="file" name="image" id="image" accept="image/*">
```

​	- `accept="image/*"` 는 업로드 가능한 이미지 파일만 보여줌

