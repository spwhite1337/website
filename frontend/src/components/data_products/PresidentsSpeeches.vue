<template>
  <div class="container">
    <hr>
    <p>Presidents Speeches</p>
    <button @click="presidentsSpeeches">Search Presidents</button>
    <input v-model="query" type="text">
      <ul v-for="result in results" :value="result.president">
          <li>{{ result.president }}  {{ result.speech }}</li>
      </ul>
    <p>Output from Presidents speeches: {{ president }}</p>
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
