// Books
import AmericanGods from '@/components/blog_posts/books/AmericanGods.vue'
import AmericanPsycho from '@/components/blog_posts/books/AmericanPsycho.vue'
import BraveNewWorld from '@/components/blog_posts/books/BraveNewWorld.vue'
import CatsCradle from '@/components/blog_posts/books/CatsCradle.vue'
import DorianGray from '@/components/blog_posts/books/DorianGray.vue'
import Frankenstein from '@/components/blog_posts/books/Frankenstein.vue'
import GreatGatsby from '@/components/blog_posts/books/GreatGatsby.vue'
import GulliversTravels from '@/components/blog_posts/books/GulliversTravels.vue'
import Lolita from '@/components/blog_posts/books/Lolita.vue'
import ParadiseLost from '@/components/blog_posts/books/ParadiseLost.vue'

// Political
import JobSearch from '@/components/blog_posts/political/JobSearch.vue'

// Science
import NeverPure from '@/components/blog_posts/science/NeverPure.vue'
import Science from '@/components/blog_posts/science/Science.vue'
import PhD from '@/components/blog_posts/science/PhD.vue'

export default {
    Books: [
        {
         path: '/Blog/AmericanGods',
         name: 'AmericanGods',
         component: AmericanGods,
         title: 'American Gods',
         author: 'Neil Gaiman'
       },
       {
          path: '/Blog/AmericanPsycho',
          name: 'AmericanPsycho',
          component: AmericanPsycho,
          title: 'American Psycho',
          author: 'Bret Easton Ellis'
      },
       {
          path: '/Blog/BraveNewWorld',
          name: 'BraveNewWorld',
          component: BraveNewWorld,
          title: 'Brave New World',
          author: 'Aldous Huxley'
       },
       {
          path: '/Blog/CatsCradle',
          name: 'CatsCradle',
          component: CatsCradle,
          title: 'Cat\'s Cradle',
          author: 'Kurt Vonnegut'
       },
       {
          path: '/Blog/DorianGray',
          name: 'DorianGray',
          component: DorianGray,
          title: 'The Picture of Dorian Gray',
          author: 'Oscar Wilde'
       },
       {
          path: '/Blog/Frankenstein',
          name: 'Frankenstein',
          component: Frankenstein,
          title: 'Frankenstein',
          author: 'Mary Shelley'
       },
       {
          path: '/Blog/GreatGatsby',
          name: 'GreatGatsby',
          component: GreatGatsby,
          title: 'The Great Gatsby',
          author: 'F. Scott Fitzgerald'
       },
       {
          path: '/Blog/GulliversTravels',
          name: 'GulliversTravels',
          component: GulliversTravels,
          title: 'Gulliver\'s Travels',
          author: 'Jonathan Swift'
       },
       {
          path: '/Blog/Lolita',
          name: 'Lolita',
          component: Lolita,
          title: 'Lolita',
          author: 'Vladimir Nabokov'
       },
       {
         path: '/Blog/ParadiseLost',
         name: 'ParadiseLost',
         component: ParadiseLost,
         title: 'Paradise Lost',
         author: 'John Milton'
       }
    ],
    Political: [
      {
         path: '/Blog/JobSearch',
         name: 'JobSearch',
         component: JobSearch,
         title: 'Job Search',
      },
    ],
    Science: [
      {
        path: '/Blog/NeverPure',
        name: 'NeverPure',
        component: NeverPure,
        title: 'Never Pure by Steven Shapin',
      },
      {
        path: '/Blog/Science',
        name: 'Science',
        component: Science,
        title: 'The Definition of Science'
      },
      {
        path: '/Blog/Science',
        name: 'PhD',
        component: PhD,
        title: 'My PhD Summary'
      }
    ]
}