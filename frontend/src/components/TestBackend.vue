<template>
  <div class="hello">
    <button @click="testBackend">Call backend</button>
    <h2>{{ test.test }}</h2>
  </div>
</template>

<script>
import axios from 'axios'
const path = 'http://localhost/api/test'
export default {
  name: 'TestBackend',
  data () {
    return {
      test: 'none'
    }
  },
  methods: {
    testBackend () {
      axios.get(path).then(response => {
        this.test = response.data.test
        })
        .catch(error => {
          console.log(error)
          })
          return {}
        }
      }
}
</script>
