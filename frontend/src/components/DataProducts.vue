<template>
  <div>
    <p>Data Products</p>

    <!--  Product Selector  -->
    <div class="container">
      <b-form-select v-model="data_product" :options="data_products" size="sm" class="mt-3"></b-form-select>
    </div>

    <!--   Sports Bettors   -->
    <div>
      <hr>
      <p>Sports Bettors</p>
      <div class="container">
        <b-form-select v-model="random_effect" :options="random_effects" size="sm" class="mt-3"></b-form-select>
      </div>
      <button @click="sportsBettors">Bet on Sports</button>
      <input v-model="random_effect_value" type="text">
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
      // Global
      data_products: ['Sports Bettors', 'Magic Card Classifier', 'Presidents Speeches'],
      data_product: '',

      // Sports Bettors
      random_effects: ['team', 'opponent'],
      random_effect: 'team',
      random_effect_value: '',
      sb_output: '',

      // Presidents - Speeches
      query: '',
      president: '',

      // Card Classifier
      input_path: '',
      card_color: ''
    }
  },
  methods: {
    sportsBettors () {
      const path = `http://localhost:5000/api/sportsbettors`
      axios.get(path, {
        params: {
          random_effect: this.random_effect,
          inputs: {
            RandomEffect: this.random_effect_value
          }
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
