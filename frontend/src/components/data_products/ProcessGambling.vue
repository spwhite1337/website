<template>
  <div class="container">
    <hr>
      <div>
          <h3>Process Gambling</h3>
          <p>
            Test page for gambling AI assist or whatever I call it.
              <br><br>
              The code and results can be found
              <a href="https://github.com/spwhite1337/process-gambling" target="_blank">here</a>.
          </p>
      </div>
      <div>
          <button @click="processGambling">Show Results</button>
          <input v-model="query" type="text">
      </div>
      <div class="container" v-if="results.output">
         Test output
         <ul v-for="output in results.output" :key="output">
           <li>{{ output }} </li>
         </ul>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
const path = process.env.VUE_APP_ROOT_API.concat('/api/processgambling')

export default {
  name: 'ProcessGambling',
  data () {
    return {
      query: '',
      results: {}
    }
  },
  methods: {
    processGambling () {
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
    },
  }
}
</script>
