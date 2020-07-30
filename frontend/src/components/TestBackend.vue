<template>
  <div class="hello">
    <button @click="testBackend1">Call backend</button>
    <button @click="testBackend2">Call backend</button>
    <button @click="testBackend3">Call backend</button>
    <h2>{{ test.test }}</h2>
  </div>
</template>

<script>
import axios from 'axios'
const path1 = 'http://localhost/api/test'
const path2 = '/api/test'
const path3 = 'http://backend:5000/api/test'
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
        }
      },
    testBackend2 () {
      axios.get(path2).then(response => {
        this.test = response.data.test
        })
        .catch(error => {
          console.log(error)
          })
          return {}
        }
      },
    testBackend3 () {
      axios.get(path3).then(response => {
        this.test = response.data.test
        })
        .catch(error => {
          console.log(error)
          })
          return {}
        }
      },
}
</script>
