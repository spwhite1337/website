<template>
  <div>
    <p>Data Products</p>
    <a href="./">Return Home</a>

    <!--  Product Selector  -->
    <b-dropdown id="dropdown-left" text="Left align" variant="primary" class="m-2">
      <b-dropdown-item href="#">Action</b-dropdown-item>
      <b-dropdown-item href="#">Another action</b-dropdown-item>
      <b-dropdown-item href="#">Something else here</b-dropdown-item>
    </b-dropdown>

    <!--   Sports Bettors   -->
    <div>
      <hr>
      <p>Sports Bettors</p>
      <button @click="sportsBettors">Bet on Sports</button>
      <input v-model="team" type="text">
      <p>Output from Sports Bettors: {{ sb_output }}</p>
    </div>

    <!--  Presidents Speeches  -->
    <div>
      <hr>
      <p>Presidents Speeches</p>
      <button @click="presidentsSpeeches">Search Presidents</button>
      <input v-model="query" type="text">
      <p>Output from Presidents speeches: {{ president }}</p>
    </div>

    <!--  Card Classifier  -->
    <div>
      <hr>
      <p>Card Classifier</p>
      <button @click="cardClassifier">Classify Card</button>
      <input v-model="input_path" type="text">
      <p>Output from Card Classifier: {{ card_color }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      // Sports Bettors
      team: 'Select team',
      sb_output: 'Nothing',
      // Presidents - Speeches
      query: 'Nothing',
      president: 'Nobody',
      // Card Classifier
      input_path: 'None',
      card_color: 'None'
    }
  },
  methods: {
    sportsBettors () {
      const path = `http://localhost:5000/api/sportsbettors`
      axios.get(path, {
        params: {
          team: this.team
        }
      })
        .then(response => {
          this.sb_output = response.data.sb_output
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    },
    presidentsSpeeches () {
      const path = `http://localhost:5000/api/presidentsspeeches`
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
    },
    cardClassifier () {
      const path = `http://localhost:5000/api/cardclassifier`
      axios.get(path, {
        params: {
          input_path: this.input_path
        }
      })
        .then(response => {
          this.card_color = response.data.card_color
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    }
  },
  created () {
  }
}
</script>
