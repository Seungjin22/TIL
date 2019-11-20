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
// Object destructuring
import { mapGetters } from 'vuex'
// import jwtDecode from 'jwt-decode'

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
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId'
    ])
  },
  methods: {
    // jwt가 session 안에 있는지 여부로 로그인 여부 확인 가능
    checkLoggedIn() {
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
    getTodos() {
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}`, this.requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      // requestForm -> 빈 Object
      const requestForm = new FormData()
      requestForm.append('user', this.userId)
      requestForm.append('title', title)

      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, this.requestHeader)
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
