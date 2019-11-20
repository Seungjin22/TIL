# Django & Vue js

Django(서버) + Vue js(클라이언트)

#### JWT(Json Web Token)

Json (JavaScript Object Notation)

: 자바 스크립트 객체 표기법 (Object X, 단순 String)



1. ##### Authorization

   : 권한 있는지 확인하는 여부

2. ##### Information Exchanges

   : 정보를 교환할 때



Header Payload signature

####    xxxx.yyyy.zzzz

token의 type과 사용 algorithm



라이브러리 사용하면 알아서 JWT 생성해주기 때문에 신경쓸 필요 없음



#### CORS (Cross-Origin Resource Sharing)

: HTTP 헤더를 사용하여 브라우저가 한 출처에서 힐행 중인 웹 어플리케이션에 대해 접근 권한을 부여하는 매커니즘

- 즉, 도메인/포트가 다른 서버의 자원을 요청
- But, 일반적으로 브라우저에서 보안을 이유로 CORS 요청 차단

![image](https://user-images.githubusercontent.com/22102664/69018473-ffb35d00-09ef-11ea-91d6-5861ceed060e.png)



Django 8000번 포트, Vue js 8080 포트

--> 서버(Django)에서 cross-origin HTTP 요청 허가 | **whitelisting**





  

```text
$ vue create todo-front

Vue CLI v4.0.5
? Please pick a preset: default (babel, eslint)
```



GUI 베타버전 (현재 프로젝트 맞는지 확인 필수!)

```text
$ vue ui
```

![image](https://user-images.githubusercontent.com/22102664/69021739-33947f80-09fc-11ea-9cd0-7faeda249ce2.png)



![image](https://user-images.githubusercontent.com/22102664/69021818-76565780-09fc-11ea-849c-6213d6719bd9.png)

활성화 시켜주지 않으면 #(해쉬뱅) 붙음 ==> 꼭 활성화 시켜주자! (history mode: ON)



router : route(경로)와 component 연결



1. todo-front/src/views/Login.vue 생성
2. todo-front/src/router/index.js에서 설정

```js
// 로그인 뷰 가져오기
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
    // route 설정
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]
```

3. App.vue 에서 router-link 작성

```vue
<template>
  <div id="app">
    <div id="nav">
      <!-- 라우터 지원앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트, 목표위치는 to로 지정 -->
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <router-view/>
  </div>
</template>
```

4. todo-front/src/components/LoginForm.vue 생성

```vue
<!-- LoginForm.vue -->
<template>
  <div class="login-div">
    <div class="form-group">
      <label for="id">ID</label>
      <input type="text" class="form-control" id="id" placeholder="아이디를 입력해주세요.">
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" class="form-conrol" id="password" placeholder="비밀번호를 입력해주세요.">
    </div>
    <button class="btn btn-primary">로그인</button>
  </div>
</template>
```

5. Login component에서 등록해주기!

```vue
<!-- Login.vue -->
<template>
  <div class="login">
    <LoginForm/>
  </div>
</template>

<script>
// @ -> alias to src
import LoginForm from '@/components/LoginForm'

export default {
  name: 'Login',
  components: {
    LoginForm,
  }
}
</script>
```



5. LoginForm 작성 (Form 유효성 검사 조건문 포함)



6. axios 설치 및 불러오기

```text
$ npm i axios


// LoginForm.vue

<script>
  import axios from 'axios'
  -> 상대 경로 유일하게 설정하지 않는게 모듈
```



7. 필요한 라이브러리 3개 설치

```text
$ pip install djangorestframework djangorestframework-jwt django-cors-headers
```



8. todo-back/settings.py 설정

```python
INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
]


# 구글 검색 : django-rest-framework-jwt >> Usage 아래 코드 복사
# https://jpadilla.github.io/django-rest-framework-jwt/

REST_FRAMEWORK = {
    # 로그인 여부를 확인하는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 인증 여부(JWT 소유 여부)를 확인하는 클래스
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# SECRET_KEY는 쉿! 비밀이야! 그래서 이따가 숨겨줘야해!
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
}
```



todo-front/src/components/LoginForm.vue

9. div  tag => form tag로 변경

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>

   	// form 태그는 action이 앞선다. --> @submit.prevent
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>

      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input
        type="text"
        class="form-control"
        id="id"
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
        type="password"
        class="form-control"
        id="password"
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      //1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        //2. loading의 상태를 true로 변경하고(spinner-border 돈다.)
        this.loading = true
        //3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.get('http://127.0.0.1:8000/', this.credentials)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        console.log('로그인 실패')
      }
    },
    // checkForm: Form 유효성 검사
    checkForm() {
      this.errors = []
      //1. 사용자가 아이디를 입력하지 않은 경우
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      }
      //2. 패스워드가 8글자 미만인 경우
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.")
      }
      //3. 아이디와 패스워드 모두 잘 입력한 경우
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>

<style>

</style>
```



```python
# todo-back/settings.py

JWT_AUTH = {
    # JWT encrypt함!! (SECRET_KEY는 절대 외부 노출 금지!!)
    'JWT_SECRET_KEY': SECRET_KEY,
    # JWT 해싱 알고리즘
    'JWT_ALGORITHM': 'HS256',
    # 토큰 갱신 허용 여부
    'JWT_ALLOW_REFRESH': True,
    # 1주일간 유효한 토큰 - default 5분
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 28일마다 토큰 갱신
    'JWT_REFRESH_EXPIRATION_DEL': datetime.timedelta(days=28),
}
```



#### django-cors-headers 사용법

https://github.com/adamchainz/django-cors-headers

```python
# todo-back/settings.py

# 최상단에 넣어주기!!
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ORIGIN_ALLOW_ALL = True
```

### `CORS_ORIGIN_ALLOW_ALL`

If `True`, the whitelist will not be used and all origins will be accepted. Defaults to `False`.

### `CORS_ORIGIN_WHITELIST`

A list of origins that are authorized to make cross-site HTTP requests. Defaults to `[]`.





#### django-rest-framework-jwt 사용법

https://jpadilla.github.io/django-rest-framework-jwt/

```python
# todo-back/urls.py

# username & password with POST request -> token 줌
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    ...
    path('api-token-auth/', obtain_jwt_token),
]
```



모델링하기!

```python
# todo-back/todos/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
# todo-back/settings.py

AUTH_USER_MODEL = 'todos.User'
```



```text
$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver

http://127.0.0.1:8000/api-token-auth/ 로 이동 -> 관리자 계정으로 로그인 -> JWT 만들어줌
```



terminal split

- todo-back

  ```text
  $ python manage.py runserver
  ```

- todo-front

  ```text
  $ npm run serve
  ```



vue-session 설치

```text
$ npm i vue-session
```

```js
// todo-front/src/views/main.js
import VueSession from 'vue-session'

Vue.use(VueSession)
```



```vue
<!-- todo-front/src/components/LoginForm.vue -->

<script>
import router from '../router'
    ...
</script>
```



로그인 > F12 > Application > Session Storage > vue-session-key 확인 가능

```vue
<!-- todo-front/src/views/Home.vue -->

<template>
  <div class="home">
    <h1>Todo with Django</h1>
  </div>
</template>

<script>
import router from '../router'

export default {
  name: 'home',
  components: {

  },
  methods: {
    // jwt가 session 안에 있는지 여부로 로그인 여부 확인 가능
    checkLoggedIn() {
      this.$session.start()
      // session에 jwt라는 키가 없으면! -> 로그인 시켜주겠다.
      if (!this.$session.has('jwt')) {
        router.push('/login')
      }
    }
  },
  mounted() {
    this.checkLoggedIn()
  }
}
</script>

```

이제 서버 켜면 바로 로그인 화면 뜸!



serializers.py 파일 만들기

```text
$ touch todo-back/todos/serializers.py
```

```python
# serializers.py

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)
```

```python
# todo-back/urls.py

urlpatterns = [
    ...
    path('api/v1/', include('todos.urls')),
]
```

```python
# todos/urls.py 파일 생성

from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
]
```



completed 는 default로 잡아둬서 Todo 만들어지면 자동으로 동작함



```python
# todo-back/todos/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from .models import Todo
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer

User = get_user_model()

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save() # Todo 라는 모델의 인스턴스가 나옴
        # serializer.data -> Json ({ 'id': 1, 'user': 1, 'title': 첫 번째 할 일, 'completed': false })
        return Response(serializer.data)
    return Response(status=400)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        # 기존 todo에서 request.POST(수정 내용)으로 변경
        serializer = TodoSerializer(todo, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # save하고 Json으로 응답
            return Response(serializer.data)
        # 유효하지 않으면 에러 메세지와 함께 400 에러
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 -> 해당하는 컨텐츠가 없는 경우(todo를 삭제했기 때문에 해당하는 todo가 존재하지 않음을 알려줌)
        return Response(status=204)

@api_view(['POST'])
# 로그인을 하지 않아도 요청 허용
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()의 return 값은 User 모델의 인스턴스
        user = serializer.save()
        # User model의 인스턴스가 갖고 있는 set_password -> 인자는 raw password가 들어감
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})

@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        # Response(status=403) 과 동일
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)
```



![image](https://user-images.githubusercontent.com/22102664/69112421-86853a00-0ac3-11ea-8730-dd1bda0a987f.png)

--> token 받음

![image](https://user-images.githubusercontent.com/22102664/69112594-f09ddf00-0ac3-11ea-8f89-d1c7d2d7afb7.png)

--> 토큰 넣어서 보내줘야!

![image](https://user-images.githubusercontent.com/22102664/69112842-a5d09700-0ac4-11ea-876e-17c6e535ba36.png)



jwt-decode 설치

```text
$ npm i jwt-decode
```



todo-front/src/components/TodoList.vue 파일 생성

Home.vue 에서 가져와주기

```vue
<template>
  ...
    <TodoList/>
  ...
</template>

<script>
...
import TodoList from '@/components/TodoList'

import axios from 'axios'
import jwtDecode from 'jwt-decode'
...
```



```vue
LoginForm.vue

<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>

    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>

      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input
        type="text"
        class="form-control"
        id="id"
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
        type="password"
        class="form-control"
        id="password"
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      //1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        //2. loading의 상태를 true로 변경하고(spinner-border 돈다.)
        this.loading = true
        //3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          // 토큰 저장
          this.$session.start()
          this.$session.set('jwt', res.data.token)
          // 저장 끝난 후 home으로 이동
          router.push('/')
          console.log(res)
        })
        .catch(err => {
          this.loading = false
          console.log(err)
        })
      } else {
        console.log('로그인 실패')
      }
    },
    // checkForm: Form 유효성 검사
    checkForm() {
      this.errors = []
      //1. 사용자가 아이디를 입력하지 않은 경우
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      }
      //2. 패스워드가 8글자 미만인 경우
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.")
      }
      //3. 아이디와 패스워드 모두 잘 입력한 경우
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>

<style>

</style>
```

```vue
TodoList.vue

<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed }">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">❎</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
      .then(res => {
        console.log(res)
        const targetTodo = this.todos.find(function(el) {
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        // 인덱스 -1이면 가장 오른쪽 위치니까 0부터 되도록
        if (idx > -1) {
          this.todos.splice(idx, 1)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const requestForm = new FormData()
      requestForm.append('completed', !todo.completed)
      requestForm.append('user', todo.user)
      requestForm.append('id', todo.id)
      requestForm.append('title', todo.title)
      console.log(!todo.completed, todo.user, todo.id, todo.title)

      axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, requestHeader)
      .then(res => {
        console.log(res)
        todo.completed = !todo.completed
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: rgb(112, 112, 112)
  }
</style>
```







container >> row >> col



updated() {} 는 어떤 역할?

==> watch와 비슷

---



# Vuex

: 상태 관리를 해줌



State, Getters, Mutations, Actions

State: 상태 정보를 담고 있음

Getters: return되는 어떤 값 (상태를 변화시키는게 X) --> computed 사용

Mutations: 상태를 변화시키는 애 --> 무조건 동기적으로!

Actions: 동기, 비동기 모든 로직 들어있음



```text
$ vue ui

=> vuex 플러그인 설치
```



dispatch는 actions의 함수를 부를 때

computed는 mutations의 함수를 부를 때