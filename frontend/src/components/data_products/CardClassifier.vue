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
      In the future I will enable you to upload an arbitrary image, but I'm too cheap to beef up my server at this time.
      <br><br>
      The code and results can be found <a href="https://github.com/spwhite1337/card-classifier" target="_blank">
      here</a>.
    </p>
    <hr>
    <div class="container">
      <b-form-select v-model="selection" :options="default_cards" size="sm" class="mt-3"></b-form-select>
    </div>
    <div class="container">
      <!--      <p>Model is too big to serve right now</p>-->
      <button @click="cardClassifierDefault">Classify Card</button>
      <br><br>
      <img :src="display" alt="Input Card" width="25%">
      <br><br>
      <p>Output from Card Classifier: {{ images }}</p>
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
      default_cards: [
        'Balrog', 'Galadriel', 'Javert', 'Jean', 'Link', 'Mary', 'Napolean', 'Sauron', 'Tolstoy', 'Vader'
      ],
      default_cards_f: {
        Balrog: 'balrog.jpg',
        Galadriel: 'galadriel.jpg',
        Javert: 'javert.jpg',
        Jean: 'jean.jpg',
        Link: 'link.jpg',
        Mary: 'mary.jpg',
        Napolean: 'napolean.jpg',
        Sauron: 'sauron.jpg',
        Tolstoy: 'tolstoy.jpg',
        Vader: 'vader.jpeg'
      },
      selection: '',
      output: '',
    }
  },
  computed: {
    display: function () {
      if (this.default_cards.includes(this.selection)) {
        return this.getImgUrl(this.default_cards_f[this.selection])
      }
      else {
        return this.getImgUrl('colorless.png')
      }
    },
    images: function () {
      return this.output
    },
  },
  methods: {
    cardClassifierDefault () {
      axios.get(path, {
        params: {
          selection: this.default_cards_f[this.selection]
        }
      })
        .then(response => {
          this.output = response.data.card_color
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    },
    getImgUrl (pic) {
        return require('@/assets/data_products/card_classifier/' + pic)
    }
  }
}
</script>
