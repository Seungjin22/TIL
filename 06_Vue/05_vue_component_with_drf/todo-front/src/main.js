import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

// DOM과 Vue instance를 연결
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
