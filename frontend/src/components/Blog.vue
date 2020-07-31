<template>
  <div>
    <p>Blog Posts</p>
    <ul>
      <li><button @click="showNeverPure">Never Pure by Steven Shapin</button></li>
      <li><button @click="showGreatGatsby">The Great Gatsby by F. Scott Fitzgerald</button></li>
    </ul>
    <div v-if="displayNeverPure"><NeverPure/></div>
    <div v-if="displayGreatGatsby"><GreatGatsby/></div>
  </div>
</template>

<script>
  import NeverPure from './blog_posts/NeverPure.vue'
  import GreatGatsby from './blog_posts/GreatGatsby.vue'

  export default {
    data () {
      return {
        displayNeverPure: false,
        displayGreatGatsby: false
      }
    },
    components: {
      NeverPure,
      GreatGatsby
    },
    methods: {
      showNeverPure: function () {
        this.displayNeverPure = !this.displayNeverPure
      },
      showGreatGatsby: function () {
        this.displayGreatGatsby = !this.displayGreatGatsby
      }
    }
  }
</script>