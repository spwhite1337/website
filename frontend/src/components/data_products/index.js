import CardClassifier from '@/components/data_products/CardClassifier.vue'
import PresidentsSpeeches from '@/components/data_products/PresidentsSpeeches.vue'
import SportsBettors from '@/components/data_products/SportsBettors'

export default [
    {
        path: '/DataProducts/CardClassifier',
        name: 'CardClassifier',
        component: CardClassifier,
        title: 'Magic Card Classifier'
    },
    {
        path: '/DataProducts/PresidentsSpeeches',
        name: 'PresidentsSpeeches',
        component: PresidentsSpeeches,
        title: 'Presidents Speeches Search Engine'
    },
    {
        path: '/DataProducts/SportsBettors',
        name: 'SportsBettors',
        component: SportsBettors,
        title: 'Sports Betting Aid'
    }
]