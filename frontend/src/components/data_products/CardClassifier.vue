<template>
  <div class="container">
    <hr>
    <h3>Magic The Gathering Card Classifier</h3>
    <p>
      In the days of my youth I had a handful of Magic the Gathering decks (I played Blue / White) and thoroughly
      enjoyed the artwork and creativity that went into the card design. Recent advancements in non-linear operators
      like Neural Networks have enabled very impressive modeling of high-dimensional systems such as artwork images.
      <br><br>
      A collection of Magic Card images were collected from <a href="https://mtgjson.com/" target="_blank">
      mtgjson.com</a> and used to create a mana-classifier with the Keras API. Select an image from the default 
      drop-down list to see the mana-class it would belong to if it were incorporated into the MTG catalog.
      <br><br>
      In the future I will enable you to upload an arbitrary image, but I"m too cheap to beef up my server at this time.
      <br><br>
      The code and results can be found <a href="https://github.com/spwhite1337/card-classifier" target="_blank">
      here</a>.
    </p>
    <div class="container">
      <b-form-select v-model="default_card" :options="default_cards" size="sm" class="mt-3"></b-form-select>
    </div>
    <div class="container">
      <!--      <p>Model is too big to serve right now</p>-->
      <button @click="cardClassifier">Classify Card</button>
      <p>Output from Card Classifier: {{ card_color }}</p>
    </div>
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
