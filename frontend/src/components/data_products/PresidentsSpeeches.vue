<template>
  <div class="container">
    <hr>
    <p>Presidents Speeches</p>
    <button @click="presidentsSpeeches">Search Presidents</button>
    <input v-model="query" type="text">
  </div>
</template>

<script>
import axios from 'axios'
const path = process.env.VUE_APP_ROOT_API.concat('/api/presidentsspeeches')

export default {
  name: 'PresidentsSpeeches',
  data () {
    return {
      query: '',
    }
  },
  methods: {
    presidentsSpeeches () {
      axios.get(path, {
        params: {
          query: this.query
        }
      })
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    }
  }
}
</script>
