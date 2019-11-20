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
      errors: [],
    }
  },
  computed: {
    loading: function() {
      return this.$store.state.loading
    }
  },
  methods: {
    login() {
      //1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        //2. loading의 상태를 true로 변경하고(spinner-border 돈다.)
        this.$store.dispatch('startLoading')
        //3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          this.$store.dispatch('endLoading')
          this.$store.dispatch('login', res.data.token)
          // 저장 끝난 후 home으로 이동
          router.push('/')
        })
        .catch(err => {
          this.$store.dispatch('endLoading')
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