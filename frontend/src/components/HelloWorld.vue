<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="presidentsSpeeches">call flask</button>
    <h2>{{ president }}</h2>
  </div>
</template>

<script>
import axios from 'axios'
const path = 'http://backend:8888/api/presidentsspeeches'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      president: 'none'
    }
  },
  methods: {
    presidentsSpeeches () {
      axios.get(path).then(response => {
        this.president = response.data.president
        })
        .catch(error => {
          console.log('Here we are')
          console.log(error)
          })
          return {}
        }
      }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
