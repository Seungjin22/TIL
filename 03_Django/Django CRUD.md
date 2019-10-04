# Django CRUD



![](noteimage/structure.png)

### 1. 가상환경 구축 / 프로젝트 생성 / 앱 등록

1. 가상환경할 폴더에서 시작 (`venv`라는 가상환경을 `venv`라는 이름으로 사용하겠다)

   `$ python -m venv venv`

2. 그 다음 활성화시키기 위해 (가상환경 끄려면 `deactivate`)

   `$ source venv/Scripts/activate`

3. 확인하기 위해 

   `$ pip list`

4. django 설치

   `$ pip install django`

5. 프로젝트 생성 (프로젝트 이름 : crud)

   `$ django-admin startproject 프로젝트이름 .`

6. 앱 생성 (앱 이름 : articles)

   `$ python manage.py startapp 앱이름`

7. 앱 등록하기

   `settings.py`에서 INSTALLED_APPS 안에 앱 이름 등록

   

   > ```python
   > # settings.py 설정하기
   > 
   > # TEMPLATES 안 'DIRS' 설정
   > 'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
   > 
   > # 언어, 시간 설정
   > LANGUAGE_CODE = 'ko-kr'
   > 
   > TIME_ZONE = 'Asia/Seoul'
   > ```



### 2. Modeling

1. models.py에 테이블 정의

   ```python
   from django.db import models
   
   class Article(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       def __str__(self):
           return f'제목: {self.title}, 내용: {self.content}'
   ```

   

2. make migrations을 통해 설계도 만들기 ==> (앱 등록!! 해야 가능)

   `$ python manage.py makemigrations`

   

   migrate commit 메세지 확인

   `$ python manage.py sqlmigrate articles 0001`

   migrate 상태 보기

   `$ python manage.py showmigrations`



3. migrate를 통해 데이터베이스에 반영

   `$ python manage.py migrate`



### 3. 기본 틀 만들기 |`base.html`, `templates`, `urls.py`/앱 아래 

1. `base.html` 구성하기 (Bootstrap 탭 가져오기)

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
       <title>Document</title>
   </head>
   <body>
       <h1 class="text-center">CRUD</h1>
       <div class="container">
           {% block body %}
           {% endblock %}
       </div>
       <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   ==> 이렇게 만든 `base.html`을 다른 html 파일에서 사용 가능

   ```html
   <!-- 다른 .html -->
   {% extends 'base.html' %}
   
   {% block body %}
   {% endblock %}
   ```



2. 앱 아래에 `templates` 폴더 만들기

   ```text
   articles
   	templates
   		articles
   ```

   ==> name space 구분을 위해 (directory별 인위적으로 구분!)

   ​	   같은 이름의 html 파일이 있더라도 어느 앱에 해당하는건지 구분해주기 위함



3. 앱 아래 `urls.py` 파일 만들기

   ==> 한 곳에 몰빵할시 순서에 따라 접근되는 문제가! (전반기 수업 때 utilities 앱 하나 더 만들었을 때 참고)

   ​		INSTALLED_APPS에 등록된 순서대로 접근함

   - `urls.py(/프로젝트)` : 오리지널. 문지기 역할(어떤 앱으로 뿌려줄건지)

   - `urls.py(/앱)`













