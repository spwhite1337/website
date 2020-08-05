<template>
  <div class="container">
    <hr>
    <p>Card Classifier</p>
    <div class="container">
      <b-form-select v-model="default_card" :options="default_cards" size="sm" class="mt-3"></b-form-select>
    </div>
<!--      <p>Model is too big to serve right now</p>-->
    <button @click="cardClassifier">Classify Card</button>
    <p>Output from Card Classifier: {{ card_color }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const path = process.env.VUE_APP_ROOT_API.concat('/api/cardclassifier')

export default {
  name: 'CardClassifier',
  data () {
    return {
      default_cards: ['balrog', 'galadriel', 'javert', 'jean', 'link', 'mary', 'napolean', 'sauron', 'tolstoy', 'vader'],
      default_card: '',
      card_color: ''
    }
  },
  methods: {
    cardClassifier () {
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
  }
}
</script>
