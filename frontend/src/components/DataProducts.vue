<template>
  <div>
    <p>Data Products</p>

    <!--  Product Selector  -->
    <div class="container">
      <b-form-select v-model="data_product" :options="data_products" size="sm" class="mt-3"></b-form-select>
    </div>

    <!--   Sports Bettors   -->
    <div class="container" v-if="showSportsBettors">
      <hr>
      <p>Sports Bettors</p>
      <div class="container">
        <b-form-select v-model="league" :options="leagues" size="sm" class="mt-3"></b-form-select>
        <b-form-select v-model="random_effect" :options="random_effects" size="sm" class="mt-3"></b-form-select>
        <b-form-select v-model="condition" :options="conditions" size="sm" class="mt-3"></b-form-select>
      </div>
      <br>
      <input v-model="random_effect_value" type="text">
      <br><br>
      <button @click="sportsBettors">Bet on Sports</button>
      <p>Output from Sports Bettors: {{ sb_output }}</p>
    </div>

    <!--  Presidents Speeches  -->
    <div class="container" v-if="showPresidentsSpeeches"><PresidentsSpeeches/></div>

    <!--  Card Classifier  -->
    <div class="container" v-if="showCardClassifier">
      <hr>
      <p>Card Classifier</p>
      <div class="container">
        <b-form-select v-model="default_card" :options="default_cards" size="sm" class="mt-3"></b-form-select>
      </div>
      <button @click="cardClassifier">Classify Card</button>
      <p>Output from Card Classifier: {{ card_color }}</p>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import PresidentsSpeeches from './data_products/PresidentsSpeeches.vue'

export default {
  components: {
    PresidentsSpeeches
  },
  data () {
    return {
      // Global
      data_products: ['Sports Bettors', 'Magic Card Classifier', 'Presidents Speeches'],
      data_product: '',

      // Sports Bettors
      leagues: ['College Football', 'NFL'],
      league: '',
      random_effects: ['team', 'opponent'],
      random_effect: 'team',
      random_effect_value: '',
      conditions: ['RushOnly', 'PassOnly', 'Offense', 'PointsScored', 'All'],
      condition: '',
      sb_output: '',

      // Presidents Speeches
      query: '',
      president: '',

      // Card Classifier
      default_cards: ['balrog', 'galadriel', 'javert', 'jean', 'link', 'mary', 'napolean', 'sauron', 'tolstoy', 'vader'],
      default_card: '',
      card_color: ''
    }
  },
  computed: {
    showCardClassifier: function () {
      return this.data_product === 'Magic Card Classifier'
    },
    showSportsBettors: function () {
      return this.data_product === 'Sports Bettors'
    },
    showPresidentsSpeeches: function () {
      return this.data_product === 'Presidents Speeches'
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
          default_card: this.default_card
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
