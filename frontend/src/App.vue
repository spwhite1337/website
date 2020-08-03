<template>
  <div id="app">
    <h3>This Site is Very Much Under Construction.</h3>
    <router-link to="./">Home</router-link>
    <br>
    <router-link to="./DataProducts">Data Products</router-link>
    <br>
    <router-link to="./Blog">Blog</router-link>
    <br>
    <router-link to="./Contact">Contact</router-link>
    <br>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>
