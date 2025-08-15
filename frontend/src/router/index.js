import Vue from 'vue'
import Router from 'vue-router'
import DataProductsIndex from '@/components/DataProducts.vue'
import DataProducts from '@/components/data_products'
import Home from '@/components/Home.vue'
import Blog from '@/components/Blog.vue'
import Contact from '@/components/Contact.vue'
import NotFound from '@/components/NotFound.vue'
import BlogPosts from '@/components/blog_posts'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/DataProducts',
            name: 'DataProducts',
            component: DataProductsIndex,
            children: DataProducts
        },
        {
            path: '/Blog',
            name: 'Blog',
            component: Blog,
            children: BlogPosts.Books.concat(BlogPosts.Science)
        },
        {
            path: '/Contact',
            name: 'Contact',
            component: Contact
        },
        {
            path: '*',
            name: 'NotFound',
            component: NotFound
        }
    ]
})
