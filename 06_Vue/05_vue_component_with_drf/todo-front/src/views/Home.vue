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
