<template>
  <div>
    <p>Blog Posts</p>
    <ul>
      <li><button @click="showAmericanGods">American Gods by Neil Gaiman</button></li>
      <li><button @click="showAmericanPsycho">American Psycho by Bret Easton Ellis</button></li>
      <li><button @click="showBraveNewWorld">Brave New World by Aldous Huxley</button></li>
      <li><button @click="showCatsCradle">Cat's Cradle by Kurt Vonnegut</button></li>
      <li><button @click="showNeverPure">Never Pure by Steven Shapin</button></li>
      <li><button @click="showGreatGatsby">The Great Gatsby by F. Scott Fitzgerald</button></li>
      <li><button @click="showFrankenstein">Frankenstein by Mary Shelley</button></li>
      <li><button @click="showDorianGray">The Picture of Dorian Gray by Oscar Wilde</button></li>
      <li><button @click="showGulliversTravels">Gulliver's Travels by Jonathan Swift</button></li>
      <li><button @click="showLolita">Lolita by Vladimir Nabokov</button></li>
      <li><button @click="showParadiseLost">Paradise Lost by John Milton</button></li>
      <li><button @click="showScience">Science by Scott White</button></li>
      <li><button @click="showJobSearch">Job Search by Scott White</button></li>
    </ul>
    <div v-if="display === 'American Gods'"><AmericanGods/></div>
    <div v-if="display === 'American Psycho'"><AmericanPsycho/></div>
    <div v-if="display === 'Brave New World'"><BraveNewWorld/></div>
    <div v-if="display === 'Cats Cradle'"><CatsCradle/></div>
    <div v-if="display === 'Never Pure'"><NeverPure/></div>
    <div v-if="display === 'Great Gatsby'"><GreatGatsby/></div>
    <div v-if="display === 'Frankenstein'"><Frankenstein/></div>
    <div v-if="display === 'Dorian Gray'"><DorianGray/></div>
    <div v-if="display === 'Gullivers Travels'"><GulliversTravels/></div>
    <div v-if="display === 'Lolita'"><Lolita/></div>
    <div v-if="display === 'Paradise Lost'"><ParadiseLost/></div>
    <div v-if="display === 'Science'"><Science/></div>
    <div v-if="display === 'Job Search'"><JobSearch/></div>
  </div>
</template>

<script>
  import AmericanGods from './blog_posts/books/AmericanGods.vue'
  import AmericanPsycho from './blog_posts/books/AmericanPsycho.vue'
  import BraveNewWorld from './blog_posts/books/BraveNewWorld.vue'
  import CatsCradle from './blog_posts/books/CatsCradle.vue'
  import NeverPure from './blog_posts/science/NeverPure.vue'
  import GreatGatsby from './blog_posts/books/GreatGatsby.vue'
  import Frankenstein from './blog_posts/books/Frankenstein.vue'
  import DorianGray from './blog_posts/books/DorianGray.vue'
  import GulliversTravels from './blog_posts/books/GulliversTravels.vue'
  import Lolita from './blog_posts/books/Lolita.vue'
  import ParadiseLost from './blog_posts/books/ParadiseLost.vue'
  import Science from './blog_posts/science/Science.vue'
  import JobSearch from './blog_posts/political/JobSearch.vue'

  export default {
    data () {
      return {
          display: ''
      }
    },
    components: {
      AmericanGods,
      AmericanPsycho,
      BraveNewWorld,
      CatsCradle,
      NeverPure,
      GreatGatsby,
      Frankenstein,
      DorianGray,
      GulliversTravels,
      Lolita,
      ParadiseLost,
      Science,
      JobSearch
    },
    methods: {
      showAmericanGods: function () {
        this.display = 'American Gods'
      },
      showAmericanPsycho: function () {
        this.display = 'American Psycho'
      },
      showBraveNewWorld: function () {
        this.display = 'Brave New World'
      },
      showCatsCradle: function () {
        this.display = 'Cats Cradle'
      },
      showNeverPure: function () {
        this.display = 'Never Pure'
      },
      showGreatGatsby: function () {
        this.display = 'Great Gatsby'
      },
      showFrankenstein: function () {
        this.display = 'Frankenstein'
      },
      showDorianGray: function () {
        this.display = 'Dorian Gray'
      },
      showGulliversTravels: function () {
        this.display = 'Gullivers Travels'
      },
      showLolita: function () {
        this.display = 'Lolita'
      },
      showParadiseLost: function () {
        this.display = 'Paradise Lost'
      },
      showScience: function () {
        this.display = 'Science'
      },
      showJobSearch: function () {
        this.display = 'Job Search'
      }
    }
  }
</script>