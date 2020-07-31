<template>
  <div>
    <p>Blog Posts</p>
    <ul>
      <li><button @click="showNeverPure">Never Pure by Steven Shapin</button></li>
      <li><button @click="showGreatGatsby">The Great Gatsby by F. Scott Fitzgerald</button></li>
      <li><button @click="showFrankenstein">Frankenstein by Mary Shelley</button></li>
      <li><button @click="showDorianGray">The Picture of Dorian Gray by Oscar Wilde</button></li>
      <li><button @click="showGulliversTravels">Gulliver's Travels by Jonathan Swift</button></li>
    </ul>
    <div v-if="displayNeverPure"><NeverPure/></div>
    <div v-if="displayGreatGatsby"><GreatGatsby/></div>
    <div v-if="displayFrankenstein"><Frankenstein/></div>
    <div v-if="displayDorianGray"><DorianGray/></div>
    <div v-if="displayGulliversTravels"><GulliversTravels/></div>
  </div>
</template>

<script>
  import NeverPure from './blog_posts/NeverPure.vue'
  import GreatGatsby from './blog_posts/GreatGatsby.vue'
  import Frankenstein from './blog_posts/Frankenstein.vue'
  import DorianGray from './blog_posts/DorianGray.vue'
  import GulliversTravels from './blog_posts/GulliversTravels.vue'

  export default {
    data () {
      return {
        displayNeverPure: false,
        displayGreatGatsby: false,
        displayFrankenstein: false,
        displayDorianGray: false,
        displayGulliversTravels: false
      }
    },
    components: {
      NeverPure,
      GreatGatsby,
      Frankenstein,
      DorianGray,
      GulliversTravels
    },
    methods: {
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
      }
    }
  }
</script>