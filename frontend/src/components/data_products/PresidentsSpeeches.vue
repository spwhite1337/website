<template>
  <div class="container">
    <hr>
    <p>Presidents Speeches</p>
    <button @click="presidentsSpeeches">Search Presidents</button>
    <input v-model="query" type="text">
    <div class="container" v-if="results.length">
      Best matched Presidents
      <ul v-for="president in results.presidents" :key="president">
        <li>{{ president.toUpperCase() }}</li>
      </ul>
      Most Similar Speeches:
      <ul v-for="(speech, idx) in results.speeches" :key="speech">
        <li><a :href="speech">Speech {{ idx + 1 }}</a></li>
      </ul>
    </div>
        <div class="container" v-if="results.length > 1">
      Best matched Presidents
      <ul v-for="president in results.presidents" :key="president">
        <li>{{ president.toUpperCase() }}</li>
      </ul>
      Most Similar Speeches:
      <ul v-for="(speech, idx) in results.speeches" :key="speech">
        <li><a :href="speech">Speech {{ idx + 1 }}</a></li>
      </ul>
    </div>
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
          console.log(this.results)
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    }
  }
}
</script>
