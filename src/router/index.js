import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'
import home_page from '../views/home_page.vue'
import main_page from '../views/main_page.vue'
import search_survey from '../views/search_survey.vue'
import personal_data from '../views/personal_data.vue'
import self_message from '../views/self_message.vue'
const routes = [
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/',
    name: 'home_page',
    component: home_page
  },
  {
    path: '/main_page',
    name: 'main_page',
    component: main_page
  },
  {
    path: '/search_survey',
    name: 'search_survey',
    component: search_survey
  },
  {
    path: '/personal_data',
    name: 'personal_data',
    component: personal_data
  },  
  {
    path: '/self_message',
    name: 'self_message',
    component: self_message
  },  
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: function () {
  //     return import(/* webpackChunkName: "about" */ '../views/About.vue')
  //   }
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
