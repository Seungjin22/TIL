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

![image](https://user-images.githubusercontent.com/22102664/68168447-27480580-ffac-11e9-91d5-72f102bf3b69.png)



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

★ v-on, v-bind는 shortcut이 존재

v-bind :만 있어도 가능

v-on 약어 @



todo list에 새로운 todo를 추가해보자!

DOM을 직접 수정하는게 아니라 Vue instance를 수정해보는거 어때?



메서드: object 안에 표현된 클래스

내부 함수의 경우 화살표 써줘야 하는게 this는 무조건 젤 밖의 전역을 나타냄



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <img v-bind:src="vueImage">
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
      {{ todo.content }}
    </li>
    <li v-else v-on:click="check(todo)">[완료!]</li>
    <div>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button v-on:click="addTodo">+</button>
    </div>
    <footer>
      <button v-on:click="clearCompleted">Clear Completed</button>
    </footer>
  </div>

    <!-- view 만드는 script가 위에 여기 있어야! -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        // DOM(View)와 Vue instance(View-Model)을 연결(mount)
        el: '#app',
        data: {
          todos: [
            {
              content: '점심 메뉴 고민하기',
              completed: true,
            },
            {
              content: '사다리 타기',
              completed: false,
            },
            {
              content: '약속의 2시, 낮잠 자기',
              completed: false,
            },
            {
              content: '야자하기',
              completed: false,
            },
            {
              content: '비쥬 얼 스튜디오 설치하기',
              completed: false,
            }
          ],
          newTodo: '',
          vueImage: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTcMuMHBi03LuaJDPbiVUSzxYBKKfZ5GWdxbE2p_0o5m-CipEHX'
        },
        methods: {
          check: function(todo) {
            todo.completed = !todo.completed
          },
          addTodo: function() {
            this.todos.push({
              content: this.newTodo,
              completed: false,
            })
            // value clear
            this.newTodo = ''
          },
          clearCompleted: function() {
            const notCompletedTodos = this.todos.filter(todo => {
              return !todo.completed
            })
            this.todos = notCompletedTodos
          }
        }
      })
    </script>
</body>
</html>
```



styling | {} 안에 key: value 형태로!

```html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">
```



```html
<li v-for="todo in todos" v-bind:class="{ completed: todo.completed }">
```

```html
<li v-for="todo in todos" v-bind:class="todo.completed ? 'completed' : ''">
```

이렇게 삼항연산자로도 변경 가능





active에서 체크박스 완료해도 바로 없어지지 않는 문제 ㅠㅠ

==> id 값 부여!



directive text (v-text / v-html / v-if / v-show)

```html
<div id="app">
    <span v-text="name"></span>
    <span>{{ name }}</span>

    {{ name2 }}
    <span v-html="name2"></span>

    <p v-if="false">{{ name3 }}</p>
    <p v-show="false">{{ name3 }}</p>
  </div>
```



v-if: 조건 맞지 않으면 렌더링 X

v-show: 조건 맞지 않아도 일단 렌더링은 함



![image](https://user-images.githubusercontent.com/22102664/68175367-55394400-ffc4-11e9-8c88-145d0447e5fe.png)

==> 연결되어 있기 때문에 상호간 조작 가능







```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .todo-list {
      display: inline-block;
      width: 33%;
    }
  </style>
  
</head>
<body>
  <div id="app">
    <div class="todo-list">
      <h2>취업 준비</h2>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <li v-for="todo in todos" :key="todo.id">
        <span>{{ todo.content }}</span>
        <button @click="removeTodo(todo.id)">x</button>
      </li>
    </div>
    <div class="todo-list">
      <h2>SSAFY</h2>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <li v-for="todo in todos" :key="todo.id">
        <span>{{ todo.content }}</span>
        <button @click="removeTodo(todo.id)">x</button>
      </li>
    </div>
    <div class="todo-list">
      <h2>기타</h2>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <li v-for="todo in todos" :key="todo.id">
        <span>{{ todo.content }}</span>
        <button @click="removeTodo(todo.id)">x</button>
      </li>
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        todos: [],
        newTodo: '',
      },
      methods: {
				addTodo: function() {
          if (this.newTodo.length !== 0) {
            this.todos.push({
              id: Date.now(),
              content: this.newTodo,
              completed: false,
            })
            this.newTodo = ''
          }
				},
				// 어제는 clearCompleted로 한번에 완료된 목록 삭제
				// 이번에는 특정 todo를 삭제!
				removeTodo: function(todoId) {
          this.todos = this.todos.filter(todo => {
            return todo.id !== todoId
          })
				}
      }
    })
  </script>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    .todo-list {
      display: inline-block;
      width: 33%;
    }
  </style>
  
</head>
<body>
  <div id="app">
    <div class="todo-list">
      <h2>취업 준비</h2>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <li v-for="todo in todos" :key="todo.id">
        <span>{{ todo.content }}</span>
        <button @click="removeTodo(todo.id)">x</button>
      </li>
    </div>
    <div class="todo-list">
      <h2>SSAFY</h2>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <li v-for="todo in todos" :key="todo.id">
        <span>{{ todo.content }}</span>
        <button @click="removeTodo(todo.id)">x</button>
      </li>
    </div>
    <div class="todo-list">
      <h2>기타</h2>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <li v-for="todo in todos" :key="todo.id">
        <span>{{ todo.content }}</span>
        <button @click="removeTodo(todo.id)">x</button>
      </li>
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        todos1: [],
        newTodo: '',
      },
      methods: {
          addTodo1: function() {
          if (this.newTodo.length !== 0) {
            this.todos.push({
              id: Date.now(),
              content: this.newTodo,
              completed: false,
            })
            this.newTodo = ''
          }
				},
				removeTodo: function(todoId) {
          this.todos = this.todos.filter(todo => {
            return todo.id !== todoId
          })
				}
      }
    })
  </script>
</body>
</html>
```







---



```text
const greeting = function() {
	console.log(this)
}

greeting
ƒ () {
	console.log(this)
}

greeting()
VM317:2 Window {parent: Window, postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, …}

const you = {
    name: 'Seungjin',
    greeting
}

you.greeting()
VM317:2 {name: "Seungjin", greeting: ƒ}
```



arrow는 무조건 상위(바로 한 단계 상위)!!

​	함수 내 함수일 때, ==> vue 인스턴스

function은 전역을 가리킨다. nested하면 window를 가리킨다!

​	함수 내 함수일 때, ==> Window!



