<template>
  <div>
    <p>Blog Posts</p>
      <b-dropdown>

      <b-dropdown-item>
        <router-link :to="{ name: 'AmericanGods' }">
            American Gods
        </router-link>
    </b-dropdown-item>
            <b-dropdown-item>
        <router-link :to="{ name: 'AmericanPsycho' }">
            American Psycho
        </router-link>
    </b-dropdown-item>
      </b-dropdown>
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