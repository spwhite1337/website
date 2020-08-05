<template>
  <div>
    <p>Blog Posts</p>
    <ul>
      <b-dropdown-item>
        <router-link :to="{ name: 'AmericanGods' }">
            American Gods
        </router-link>
    </b-dropdown-item>
      <li><router-link :to="{ name: 'AmericanGods' }">American Gods By Neil Gaiman</router-link></li>
    </ul>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    data () {
      return {
      }
    },
  }
</script>