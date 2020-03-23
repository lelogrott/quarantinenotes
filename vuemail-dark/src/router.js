import Vue from 'vue'
import VueAnalytics from 'vue-analytics'
import Router from 'vue-router'
import Meta from 'vue-meta'

// import view
import Inbox from '@/views/Inbox'
import Starred from '@/views/Starred'
import SentMail from '@/views/SentMail'
import Draft from '@/views/Draft'
import Chat from '@/views/Chat'
import Places from '@/views/Places'
import Trash from '@/views/Trash'
import Spam from '@/views/Spam'

Vue.use(Router)

const router = new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'inbox',
      component: Inbox
    },
    {
      path: '/starred',
      name: 'starred',
      component: Starred
    },
    {
      path: '/sentmail',
      name: 'forms',
      component: SentMail
    },
    {
      path: '/draft',
      component: Draft
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
    },
    {
      path: '/places',
      name: 'places',
      component: Places
    },
    {
      path: '/trash',
      name: 'trash',
      component: Trash
    },
    {
      path: '/spam',
      name: 'spam',
      component: Spam
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
if (process.env.GOOGLE_ANALYTICS) {
  Vue.use(VueAnalytics, {
    id: process.env.GOOGLE_ANALYTICS,
    router,
    autoTracking: {
      page: process.env.NODE_ENV !== 'development'
    }
  })
}

export default router
