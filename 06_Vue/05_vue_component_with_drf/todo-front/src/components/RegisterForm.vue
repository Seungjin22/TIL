<template>
  <div class="register-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <form v-else class="register-form" @submit.prevent="register">
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
          placeholder="아이디를 입력해주세요"
          v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
          type="password" 
          class="form-control" 
          id="password" 
          placeholder="비밀번호를 입력해주세요"
          v-model="credentials.password"
        >
      </div>
      <div class="form-group">
        <label for="password-confirm">Password Confirm</label>
        <input 
          type="password" 
          class="form-control" 
          id="password-confirm" 
          placeholder="비밀번호를 다시 입력해주세요"
          v-model="credentials.passwordConfirm"
        >
      </div>
      <button type="submit" class="btn btn-primary">회원가입</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'RegisterForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirm: '',
      },
      errors: []
    }
  },
  computed: {
    loading() {
      return this.$store.state.loading
    }
  },
  methods: {
    register() {
      if (this.checkForm()) {
        this.$store.dispatch('startLoading')
        console.log(this.credentials)
        axios.post('http://localhost:8000/api/v1/users/', this.credentials)
        .then(res => {
          console.log(res)
          this.$store.dispatch('endLoading')
          alert("회원가입이 성공적으로 완료되었습니다.")
          router.push("/login")
        })
        .catch(err => {
          this.$store.dispatch('endloading')
          console.log(err)
        })
      } else {
        console.log("검증 실패")
      }
    },
    checkForm() {
      this.errors = []
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      } 
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 넣어주세요.")
      }
      if (this.credentials.password !== this.credentials.passwordConfirm) {
        this.errors.push("비밀번호가 일치하지 않습니다.")
      }
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>