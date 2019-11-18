# Django & Vue js

Django(서버) + Vue js(클라이언트)

#### JWT(Json Web Token)

Json (JavaScript Object Notation)

: 자바 스크립트 객체 표기법 (Object X, 단순 String)



1. 권한 있는지 확인하는 여부
2. 정보를 교환할 때



Header Payload signature

####    xxxx.yyyy.zzzz

token의 type과 사용 algorithm



라이브러리 사용하면 알아서 JWT 생성해주기 때문에 신경쓸 필요 없음



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



필요한 라이브러리 3개 설치

```text
$ pip install djangorestframework djangorestframework-jwt django-cors-headers
```



todo-back/settings.py 설정

```python
INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
]


# 구글 검색 : django-rest-framework-jwt >> Usage 아래 코드 복사

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









