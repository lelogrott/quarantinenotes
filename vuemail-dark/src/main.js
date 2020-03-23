import Vue from 'vue'

// Components
import './components'

// Plugins
import './plugins'

// Application imports
import App from './App.vue'
import router from './router'
import store from '@/store'

Vue.config.productionTip = false
Vue.use(require('vue-moment'))

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
