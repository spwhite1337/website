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
      <img :src="getImgUrl(display)" alt="Input Card" width="25%">
      <br><br>
      <div class="container" v-if="images.length > 1">
            Mana Class:
        <span v-for="(image, idx) in images" :key="idx"><img :src="getImgUrl(image)" width="5%"></span>
      </div>
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
      // Default card labels
      default_cards: [
        'Balrog', 'Galadriel', 'Javert', 'Jean', 'Link', 'Mary', 'Napolean', 'Sauron', 'Tolstoy', 'Vader'
      ],
      // Map default card labels to filename
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

      // Selection
      selection: '',
      // Default outputs as colorless
      output: ['N'],
      display: 'colorless.png',

      // Map colors to images
      colors: {
        N: 'colorless.png',
        B: 'black.png',
        U: 'blue.png',
        G: 'green.png',
        R: 'red.png',
        W: 'white.png'
      }
    }
  },
  computed: {
    // Display outputs as image files
    images: function () {
      let images_f = []
      this.output.forEach(color => images_f.push(this.colors[color]))
      return images_f
    },
  },
  methods: {
    // Get the calculated response of a card and display in the selection
    cardClassifierDefault () {
      // Get response from backend
      axios.get(path, {
        params: {
          selection: this.default_cards_f[this.selection]
        }
      })
        .then(response => {
          // Get output
          this.output = response.data.card_color
          // Display selected card
          this.display = this.default_cards_f[this.selection]
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
