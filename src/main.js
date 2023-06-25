import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import axios from 'axios'
import Vant from 'vant';
// import Vue from 'vue'
import 'vant/lib/index.css';
import ElementPlus from 'element-plus'
import 'element-plus/theme-chalk/index.css'
import { DropdownMenu, DropdownItem } from 'vant';
const app = createApp(App)
// 导航守卫
router.beforeEach((to, from, next) => {
    if (to.path === '/login' || to.path === '/') return next()
    const tokenStr = window.localStorage.getItem('token')
    if (!tokenStr) return next('/')
    next()
})
app.use(DropdownMenu);
app.use(DropdownItem);
app.use(ElementPlus)
app.use(router)
app.use(Vant);
app.mount('#app')


