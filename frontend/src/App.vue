<template>
  <div id="app" class="container">
    <h3>This Site is Very Much Under Construction.</h3>
    <b-nav>
      <b-nav-item><router-link :to="{ name: 'home' }">Home</router-link></b-nav-item>
      <b-nav-item><router-link :to="{ name: 'DataProducts' }">Data Products</router-link></b-nav-item>
      <b-nav-item><router-link :to="{ name: 'Blog' }">Blog</router-link></b-nav-item>
      <b-nav-item><router-link :to="{ name: 'Contact' }">Contact</router-link></b-nav-item>
    </b-nav>
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
