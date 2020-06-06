import Vue from 'vue'
import VueAnalytics from 'vue-analytics'
import Router from 'vue-router'
import Meta from 'vue-meta'

// import view
import Inbox from '@/views/Inbox'

Vue.use(Router)

const router = new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'inbox',
      component: Inbox
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return { selector: to.hash }
    }
    return { x: 0, y: 0 }
  }
})

Vue.use(Meta)

// https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: 'UA-46402500-3',
  router,
  autoTracking: {
    page: process.env.NODE_ENV !== 'development'
  }
})


export default router
