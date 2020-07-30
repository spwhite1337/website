<template>
  <div class="container">
    <hr>
    <p>Presidents Speeches from child</p>
    <button @click="presidentsSpeeches">Search Presidents</button>
    <input v-model="query" type="text">
    <p>Output from Presidents speeches: {{ president }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const path = 'http://localhost:5000/api/presidentsspeeches'
export default {
  name: 'PresidentsSpeeches',
  data () {
    return {
      query: '',
      president: ''
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
          this.president = response.data.president
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    }
  }
}
</script>
