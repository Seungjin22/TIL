# Vue js



자바스크립트 기반의 front-end framework



AJAX(Asynchronous Javascript and XML) : 비동기 요청

- 앞의 수행이 뒤의 수행을 막지 않음!
- 요청을 보내 응답이 올 때까지 기다렸다가 응답 오면 **그-때** 처리

Why 비동기? => 사용자가 언제 이벤트 발생 시킬 지 알 수 없음!

모든 페이지 아닌 특정 부분(좋아요)만 처리

==> 요청에 대한 응답 json으로



모든 정적 리소스는 최초 1번만 받음

새로운 페이지 요청시 페이지 갱신에 필요한 데이터만 전달 받음

사용자 경험(UX) 극대화, 불필요한 서버 자워 사용 X



3대장: Angular js, Vue js, React js



Django -> MVC(MTV)

Vue js -> MVVM

![image](https://user-images.githubusercontent.com/22102664/68101004-bc94bc80-ff0e-11e9-836c-e3c329e8b860.png)



View랑 ViewModel 연결되어 있음

Data binding 



##### ★ DOM과 Vue instance **연결**되어 있다!

```html
<body>
  <!-- DOM은 그냥 껍데기. 보여주기 위한 역할만 하는 곳 -->
  <div id="app">
    {{ message }}
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // Vue 코드가 작성될 곳
    const app = new Vue({ // new는 클래스라는 것
      // element. 이 아래 한 줄로 vue instance와 연결
      el: '#app',
      data: {
        message: 'Hello, Vue!'
      }
    })
  </script>
</body>
```



```html
<div id="app">
    <li v-for="todo in todos" v-if="!todo.completed">
      {{ todo.content }}
      {{ todo.completed }}
    </li>
</div>
```

[순서] 같은 노드에 있을 때,  v-for  >>>   v-if

v-on, v-bind는 shortcut이 존재 ==> :만 있어도 가능



todo list에 새로운 todo를 추가해보자!

DOM을 직접 수정하는게 아니라 Vue instance를 수정해보는거 어때?