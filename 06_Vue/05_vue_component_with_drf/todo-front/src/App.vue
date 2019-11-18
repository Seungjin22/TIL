<template>
  <div id="app">
    <div id="nav">
      <!-- 라우터 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트, 목표 위치는 to로 지정 -->
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
