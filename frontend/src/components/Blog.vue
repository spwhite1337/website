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
    </ul>
    <div v-if="displayAmericanGods"><AmericanGods/></div>
    <div v-if="displayAmericanPsycho"><AmericanPsycho/></div>
    <div v-if="displayBraveNewWorld"><BraveNewWorld/></div>
    <div v-if="displayCatsCradle"><CatsCradle/></div>
    <div v-if="displayNeverPure"><NeverPure/></div>
    <div v-if="displayGreatGatsby"><GreatGatsby/></div>
    <div v-if="displayFrankenstein"><Frankenstein/></div>
    <div v-if="displayDorianGray"><DorianGray/></div>
    <div v-if="displayGulliversTravels"><GulliversTravels/></div>
    <div v-if="displayLolita"><Lolita/></div>
    <div v-if="displayParadiseLost"><ParadiseLost/></div>
    <div v-if="displayScience"><Science/></div>
  </div>
</template>

<script>
  import AmericanGods from './blog_posts/AmericanGods.vue'
  import AmericanPsycho from './blog_posts/AmericanPsycho.vue'
  import BraveNewWorld from './blog_posts/BraveNewWorld.vue'
  import CatsCradle from './blog_posts/CatsCradle.vue'
  import NeverPure from './blog_posts/NeverPure.vue'
  import GreatGatsby from './blog_posts/GreatGatsby.vue'
  import Frankenstein from './blog_posts/Frankenstein.vue'
  import DorianGray from './blog_posts/DorianGray.vue'
  import GulliversTravels from './blog_posts/GulliversTravels.vue'
  import Lolita from './blog_posts/Lolita.vue'
  import ParadiseLost from './blog_posts/ParadiseLost.vue'
  import Science from './blog_posts/Science.vue'

  export default {
    data () {
      return {
        displayAmericanGods: false,
        displayAmericanPsycho: false,
        displayBraveNewWorld: false,
        displayCatsCradle: false,
        displayNeverPure: false,
        displayGreatGatsby: false,
        displayFrankenstein: false,
        displayDorianGray: false,
        displayGulliversTravels: false,
        displayLolita: false,
        displayParadiseLost: false,
        displayScience: false
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
      Science
    },
    methods: {
      showAmericanGods: function () {
        this.displayAmericanGods = !this.displayAmericanGods
      },
      showAmericanPsycho: function () {
        this.displayAmericanPsycho = !this.displayAmericanPsycho
      },
      showBraveNewWorld: function () {
        this.displayBraveNewWorld = !this.displayBraveNewWorld
      },
      showCatsCradle: function () {
        this.displayCatsCradle = !this.displayCatsCradle
      },
      showNeverPure: function () {
        this.displayNeverPure = !this.displayNeverPure
      },
      showGreatGatsby: function () {
        this.displayGreatGatsby = !this.displayGreatGatsby
      },
      showFrankenstein: function () {
        this.displayFrankenstein = !this.displayFrankenstein
      },
      showDorianGray: function () {
        this.displayDorianGray = !this.displayDorianGray
      },
      showGulliversTravels: function () {
        this.displayGulliversTravels = !this.displayGulliversTravels
      },
      showLolita: function () {
        this.displayLolita = !this.displayLolita
      },
      showParadiseLost: function () {
        this.displayParadiseLost = !this.displayParadiseLost
      },
      showScience: function () {
        this.displayScience = !this.displayScience
      }
    }
  }
</script>