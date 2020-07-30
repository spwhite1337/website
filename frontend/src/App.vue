<template>
  <div id="app">
    <p>
      You are in App.vue
    </p>
    <router-link to="./">Home</router-link>
    <router-link to="./DataProducts">Data Products</router-link>
    <router-link to="./Blog">Blog</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>
