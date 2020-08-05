<template>
  <div id="app">
    <h3>This Site is Very Much Under Construction.</h3>
    <router-link :to="{ name: 'home' }">Home</router-link>
    <br>
    <router-link :to="{ name: 'DataProducts' }">Data Products</router-link>
    <br>
    <router-link :to="{ name: 'Blog' }">Blog</router-link>
    <br>
    <router-link :to="{ name: 'AmericanGods' }">American Gods</router-link>
    <br>
    <router-link :to="{ name: 'Contact' }">Contact</router-link>
    <br>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>
