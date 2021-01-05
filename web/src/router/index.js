import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/pages/Login'
import GetImage from '@/components/pages/GetImage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/get_image',
      name: 'GetImage',
      component: GetImage
    }
  ]
})
