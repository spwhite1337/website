<template>
  <div id="app" class="container">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
          <ul class="navbar-nav">
            <li class="nav-item active"><router-link :to="{ name: 'home' }" class="nav-link">Home</router-link></li>
              <li class="nav-item active"><router-link :to="{ name: 'DataProducts' }" class="nav-link">Data Products
                </router-link></li>
              <li class="nav-item active"><router-link :to="{ name: 'Blog' }" class="nav-link">Blog</router-link></li>
              <li class="nav-item active"><router-link :to="{ name: 'Contact' }" class="nav-link">Contact</router-link></li>
          </ul>
      </nav>

      <div class="container">
        <transition name="slide-fade">
          <router-view></router-view>
        </transition>
      </div>
      <br>
      <hr>
      <div class="container">
        Website source code can be found in my <a href="https://github.com/spwhite1337/website" target="_blank">repo</a>.
        All software is open source. The server is from AWS.
        <br><br>
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

#app {
  padding: 1%
}
</style>
