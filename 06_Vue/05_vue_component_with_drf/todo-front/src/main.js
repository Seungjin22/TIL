import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import VueSession from 'vue-session'
import store from './store'

Vue.config.productionTip = false
// Vue.use(VueSession)

// DOM과 Vue instance를 연결
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
