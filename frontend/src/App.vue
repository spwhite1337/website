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
      <transition name="slide-fade">
        <router-view></router-view>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
  /* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
