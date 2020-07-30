<template>
  <div class="hello">
    <button @click="testBackend1">Call backend</button>
    <button @click="testBackend2">Call backend</button>
    <h2>{{ test.test }}</h2>
  </div>
</template>

<script>
import axios from 'axios'
const path1 = '/api/test'
const path2 = 'http://backend:8080/api/test'
export default {
  name: 'TestBackend',
  data () {
    return {
      test: 'none'
    }
  },
  methods: {
    testBackend1 () {
      axios.get(path1).then(response => {
        this.test = response.data.test
        })
        .catch(error => {
          console.log(error)
          })
          return {}
        },
    testBackend2 () {
      axios.get(path2).then(response => {
        this.test = response.data.test
        })
        .catch(error => {
          console.log(error)
          })
          return {}
        },
      }
}
</script>
