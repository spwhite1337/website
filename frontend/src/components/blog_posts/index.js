import AmericanGods from '@/components/blog_posts/books/AmericanGods.vue'
import AmericanPsycho from '@/components/blog_posts/books/AmericanPsycho.vue'
import BraveNewWorld from '@/components/blog_posts/books/BraveNewWorld.vue'


export default [
    { path: '/Blog/AmericanGods', name: 'AmericanGods', component: AmericanGods, label: 'American Gods' },
    { path: '/Blog/AmericanPsycho', name: 'AmericanPsycho', component: AmericanPsycho, label: 'American Psycho' },
    { path: '/Blog/BraveNewWorld', name: 'BraveNewWorld', component: BraveNewWorld, label: 'Brave New World' }
]
