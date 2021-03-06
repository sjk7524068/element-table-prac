import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '@/components/Hello.vue'
import date from '@/components/datepicker.vue'
import Socket from '@/components/socket.vue'
import Markdown from '@/components/Markdown.vue'

Vue.use(VueRouter)

  const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path:'/date',
    name:'',
    component:date
  },
  {
    path:'/socket',
      name:'',
      component:Socket
  },
  {
    path:'/mark',
      name:'',
      component:Markdown
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
