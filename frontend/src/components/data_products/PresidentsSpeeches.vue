<template>
  <div class="container">
    <hr>
    <p>Presidents Speeches</p>
    <button @click="presidentsSpeeches">Search Presidents</button>
    <input v-model="query" type="text">
    {{ results }}
      <p>Similar Presidents</p>
      <ul v-for="president in results.presidents" :key="president">
          <li>{{ president }}</li>
      </ul>
      <p>Similar Speeches</p>
      <ul v-for="speech in results.speeches" :key="speech">
          <li>{{ speech }}</li>
      </ul>
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
      results: []
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
          this.results = response.data
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    }
  }
}
</script>
