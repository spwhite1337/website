import Vue from 'vue'
import Router from 'vue-router'
import DataProducts from '@/components/DataProducts.vue'
import Home from '@/components/Home.vue'
import Blog from '@/components/Blog.vue'

Vue.use(Router)

export default new Router({
    routes: [
        { path: '/', name: 'home', component: Home},
        { path: '/DataProducts', name: 'DataProducts', component: DataProducts},
        { path: '/Blog', name: 'Blog', component: Blog}
    ]
})
