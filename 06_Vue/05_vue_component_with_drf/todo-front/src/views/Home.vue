<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    // jwt가 session 안에 있는지 여부로 로그인 여부 확인 가능
    checkLoggedIn() {
      this.$session.start()
      // session에 jwt라는 키가 없으면! -> 로그인 시켜주겠다.
      if (!this.$session.has('jwt')) {
        router.push('/login')
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          // Postman에서 headers에서 한 작업과 같음
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      // jwt 가져오기 위함
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      // requestForm -> 빈 Object
      const requestForm = new FormData()
      requestForm.append('user', user_id)
      requestForm.append('title', title)

      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, requestHeader)
      .then(res => {
        this.todos.push(res.data)
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    this.checkLoggedIn(),
    this.getTodos()
  }
}
</script>
