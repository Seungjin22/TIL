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

django built-in template tags and filters 참고



프레임워크 사용은 마치 프랜차이즈 카페 창업하는 것과 유사

우리는 프레임워크를 사용할 것이다!

python의 프레임워크 django



MVC (Model View Controller)

MTV (Model Template View) ==> django

M: 데이터를 관리

**T: 사용자가 보는 화면**

**V: 중간 관리자**

==> 우선 T & V 만 먼저!



---



1. 가상환경할 폴더에서 시작

   `python -m venv venv`

2. 그 다음 활성화시키기 위해

   `source venv/Scripts/activate`

3. 확인하기 위해 pip list

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

